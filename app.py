# app.py
"""
Aplicação Flask para o FlowTale.
Gerencia rotas para login, menu, jogo, escolhas, salvamento e conquistas, com autenticação e persistência.
"""

import os
import json
import uuid
from flask import Flask, render_template, request, session, jsonify, redirect, url_for
from menu import Menu

from historia_medieval import HistoriaMedieval
from historia_detetive import HistoriaDetetive
from historia_crononauta import HistoriaCrononauta
from historia_horror_cosmico import HistoriaHorrorCosmico

app = Flask(__name__)
app.secret_key = 'f5a8b9c2d3e4f1a2b3c4d5e6f7a8b9c2'

# Diretórios
SAVE_DIR = os.path.join(os.path.dirname(__file__), 'saves')
SESSION_DIR = os.path.join(os.path.dirname(__file__), 'sessions')  # Novo diretório para sessões
CONQUESTS_DIR = os.path.join(os.path.dirname(__file__), 'conquests')
os.makedirs(SAVE_DIR, exist_ok=True)
os.makedirs(SESSION_DIR, exist_ok=True)
os.makedirs(CONQUESTS_DIR, exist_ok=True)

# Instância global do Menu do FlowTale
menu = Menu()
menu.adicionar_historia("A Lenda do Coração de Dragão", HistoriaMedieval)
menu.adicionar_historia("O Caso do Diamante Sumido", HistoriaDetetive)
menu.adicionar_historia("Paradoxo do Crononauta", HistoriaCrononauta)
menu.adicionar_historia("O Chamado do Abismo Estelar", HistoriaHorrorCosmico)

# Definição de conquistas
CONQUISTAS = {
    "primeira_vitoria": {"nome": "Primeira Vitória", "condicao": lambda h: h.cena_atual >= len(h.cenas), "bonus": 10},
    "mestre_pontos": {"nome": "Mestre dos Pontos", "condicao": lambda h: h.pontuacao >= 20, "bonus": 15},
    "explorador": {"nome": "Explorador", "condicao": lambda h: h.nome == "Aventura Não Linear" and h.cena_atual >= len(h.cenas), "bonus": 20}
}

def listar_saves(username):
    """Retorna uma lista de saves disponíveis para o usuário."""
    saves = []
    prefix = f"save_{username}_"
    for filename in os.listdir(SAVE_DIR):
        if filename.startswith(prefix) and filename.endswith(".json"):
            save_name = filename[len(prefix):-len(".json")]
            with open(os.path.join(SAVE_DIR, filename), 'r') as f:
                data = json.load(f)
                saves.append({
                    "nome_save": save_name,
                    "nome_historia": data["nome"],
                    "pontuacao": data["pontuacao"],
                    "cena_atual": data["cena_atual"]
                })
    return saves

def carregar_conquistas(username):
    """Carrega as conquistas do usuário a partir de um arquivo JSON."""
    conquest_path = os.path.join(CONQUESTS_DIR, f"conquests_{username}.json")
    if os.path.exists(conquest_path):
        with open(conquest_path, 'r') as f:
            return json.load(f)
    return []

def salvar_conquistas(username, conquistas):
    """Salva as conquistas do usuário em um arquivo JSON."""
    conquest_path = os.path.join(CONQUESTS_DIR, f"conquests_{username}.json")
    with open(conquest_path, 'w') as f:
        json.dump(conquistas, f)

def verificar_conquistas(historia, username):
    """Verifica e desbloqueia conquistas, aplicando bônus de pontuação."""
    conquistas = carregar_conquistas(username)
    for chave, conquista in CONQUISTAS.items():
        if chave not in conquistas and conquista["condicao"](historia):
            conquistas.append(chave)
            historia.pontuacao += conquista["bonus"]
            print(f"Conquista desbloqueada: {conquista['nome']} para {username}")
    salvar_conquistas(username, conquistas)
    return conquistas

def load_session(username):
    """Carrega a sessão do usuário a partir de um arquivo, se existir."""
    session_id = session.get('session_id')
    if session_id:
        session_path = os.path.join(SESSION_DIR, f"session_{username}_{session_id}.json")
        if os.path.exists(session_path):
            with open(session_path, 'r') as f:
                return json.load(f)
    return {}

def save_session(username, data):
    """Salva a sessão do usuário em um arquivo."""
    session_id = session.get('session_id', str(uuid.uuid4()))
    session['session_id'] = session_id
    session_path = os.path.join(SESSION_DIR, f"session_{username}_{session_id}.json")
    with open(session_path, 'w') as f:
        json.dump(data, f)

@app.route("/", methods=["GET"])
def login():
    """Rota de login: exibe a tela de entrada de nome de usuário."""
    if 'username' in session:
        return redirect(url_for('index'))
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def do_login():
    """Processa o login e redireciona para o menu."""
    username = request.form.get("username")
    if not username or len(username.strip()) == 0:
        return render_template("login.html", error="Por favor, insira um nome de usuário válido.")
    session['username'] = username.strip()
    save_session(username, {})
    return redirect(url_for('index'))

@app.route("/logout", methods=["GET"])
def logout():
    """Limpa a sessão e redireciona para a tela de login."""
    username = session.get('username')
    if username:
        session_id = session.get('session_id')
        if session_id:
            session_path = os.path.join(SESSION_DIR, f"session_{username}_{session_id}.json")
            if os.path.exists(session_path):
                os.remove(session_path)
    session.clear()
    return redirect(url_for('login'))

@app.route("/menu", methods=["GET"])
def index():
    """Rota principal: exibe o menu de histórias, saves e conquistas do usuário."""
    if 'username' not in session:
        return redirect(url_for('login'))
    saves = listar_saves(session['username'])
    conquistas = carregar_conquistas(session['username'])
    conquistas_info = [{"chave": c, **CONQUISTAS[c]} for c in conquistas]
    return render_template("index.html", historias=menu.historias, saves=saves, username=session['username'], conquistas_info=conquistas_info)

@app.route("/jogar/<nome_historia>")
def jogar(nome_historia):
    """Inicia uma nova história."""
    if 'username' not in session:
        return redirect(url_for('login'))
    if nome_historia not in menu.historias:
        return "História não encontrada no FlowTale", 404
    
    session_data = load_session(session['username'])
    session_data['historia'] = None  # Limpa qualquer história anterior
    historia = menu.historias[nome_historia]()
    session_data['historia'] = historia.to_dict()
    save_session(session['username'], session_data)
    
    print(f"Iniciando {nome_historia} - Cena atual: {historia.cena_atual}")
    
    cena_atual = historia.cenas[historia.cena_atual]
    return render_template("jogo.html", cena=cena_atual, nome_historia=nome_historia, cena_atual_idx=historia.cena_atual, pontuacao=historia.pontuacao)

@app.route("/escolha", methods=["POST"])
def escolha():
    """Processa a escolha do jogador e verifica conquistas."""
    if 'username' not in session:
        return redirect(url_for('login'))
    
    session_data = load_session(session['username'])
    if 'historia' not in session_data or not session_data['historia']:
        return redirect(url_for('index'))  # Redireciona se não houver história ativa
    
    if session_data['historia'].get('nome') != request.form.get("nome_historia"):
        return "Sessão inválida ou história incorreta", 400
    
    escolha = int(request.form.get("escolha", -1))
    nome_historia = request.form.get("nome_historia")
    cena_idx_form = int(request.form.get("cena_idx", -1))
    
    if escolha < 0 or cena_idx_form < 0:
        return "Dados inválidos", 400
    
    historia_class = menu.historias[nome_historia]
    historia = historia_class.from_dict(session_data['historia'])
    
    print(f"Escolha recebida - Cena do formulário: {cena_idx_form}, Cena atual na sessão: {historia.cena_atual}")
    
    # Verifica se o jogador está na tela de jogo e se há trapaça
    if historia.cena_atual < len(historia.cenas):  # Só verifica trapaça se ainda houver cenas
        if cena_idx_form != historia.cena_atual:
            print("Possível trapaça detectada! Redirecionando para fim.")
            historia.pontuacao = -99999
            historia.cena_atual = len(historia.cenas)
            session_data['historia'] = historia.to_dict()
            save_session(session['username'], session_data)
            return render_template("fim.html", pontuacao=historia.pontuacao, mensagem="Não trapaceie! Você perdeu por manipular a navegação!")
    else:
        print("Fim normal da história")
        verificar_conquistas(historia, session['username'])
        session_data['historia'] = historia.to_dict()
        save_session(session['username'], session_data)
        return render_template("fim.html", pontuacao=historia.pontuacao)
    
    # Processa a escolha normalmente
    consequencia, correta, proxima_cena = historia.processar_escolha(escolha)
    
    print(f"Após escolha - Nova cena_atual: {historia.cena_atual}, Pontuação: {historia.pontuacao}")
    
    verificar_conquistas(historia, session['username'])
    session_data['historia'] = historia.to_dict()
    save_session(session['username'], session_data)
    
    if historia.cena_atual < len(historia.cenas):
        cena_atual = historia.cenas[historia.cena_atual]
        return render_template("jogo.html", cena=cena_atual, nome_historia=nome_historia, cena_atual_idx=historia.cena_atual, pontuacao=historia.pontuacao)
    else:
        print("Fim normal após escolha")
        return render_template("fim.html", pontuacao=historia.pontuacao)

@app.route("/salvar", methods=["POST"])
def salvar():
    """Salva o progresso atual com confirmação de sobrescrição."""
    if 'username' not in session:
        return jsonify({"error": "Usuário não autenticado"}), 401
    session_data = load_session(session['username'])
    if 'historia' not in session_data:
        return jsonify({"error": "Nenhum jogo em andamento"}), 400
    
    nome_save = request.form.get("nome_save", "padrao")
    save_path = os.path.join(SAVE_DIR, f"save_{session['username']}_{nome_save}.json")
    
    if os.path.exists(save_path):
        if request.form.get("confirmar_sobrescrever") != "true":
            return jsonify({"confirmacao": f"O save '{nome_save}' já existe. Deseja sobrescrevê-lo?"}), 409
    
    with open(save_path, 'w') as f:
        json.dump(session_data['historia'], f)
    
    return jsonify({"message": f"Progresso salvo como {nome_save}!"})

@app.route("/carregar", methods=["POST"])
def carregar():
    """Carrega um save e verifica conquistas."""
    if 'username' not in session:
        return jsonify({"error": "Usuário não autenticado"}), 401
    
    nome_save = request.form.get("nome_save", "padrao")
    save_path = os.path.join(SAVE_DIR, f"save_{session['username']}_{nome_save}.json")
    
    if not os.path.exists(save_path):
        return jsonify({"error": "Nenhum save encontrado para este nome"}), 404
    
    with open(save_path, 'r') as f:
        session_data = load_session(session['username'])
        session_data['historia'] = json.load(f)
        save_session(session['username'], session_data)
    
    historia_class = menu.historias[session_data['historia']['nome']]
    historia = historia_class.from_dict(session_data['historia'])
    
    print(f"Carregado save {nome_save} para {session['username']} - Cena atual: {historia.cena_atual}")
    
    verificar_conquistas(historia, session['username'])
    session_data['historia'] = historia.to_dict()
    save_session(session['username'], session_data)
    
    if historia.cena_atual >= len(historia.cenas):
        return render_template("fim.html", pontuacao=historia.pontuacao)
    
    cena_atual = historia.cenas[historia.cena_atual]
    return render_template("jogo.html", cena=cena_atual, nome_historia=historia.nome, cena_atual_idx=historia.cena_atual, pontuacao=historia.pontuacao)

@app.route("/apagar", methods=["POST"])
def apagar():
    """Apaga um save específico do usuário."""
    if 'username' not in session:
        return jsonify({"error": "Usuário não autenticado"}), 401
    
    nome_save = request.form.get("nome_save", "padrao")
    save_path = os.path.join(SAVE_DIR, f"save_{session['username']}_{nome_save}.json")
    
    if not os.path.exists(save_path):
        return jsonify({"error": "Nenhum save encontrado para este nome"}), 404
    
    try:
        os.remove(save_path)
        return jsonify({"message": f"Save '{nome_save}' apagado com sucesso!"})
    except Exception as e:
        return jsonify({"error": f"Erro ao apagar o save: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)