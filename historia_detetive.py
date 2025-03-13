# historia_detetive.py
"""
Define a história de detetive 'O Caso do Diamante Sumido' para o FlowTale.
História não linear com múltiplas pistas, suspeitos e finais baseados nas escolhas.
"""

from cena import Cena

class HistoriaDetetive:
    def __init__(self):
        self.nome = "O Caso do Diamante Sumido"
        self.linear = False
        self.cenas = self.inicializar_cenas()
        self.cena_atual = 0
        self.pontuacao = 0

    def inicializar_cenas(self):
        """Inicializa as cenas da aventura de detetive."""
        cenas = [
            # Cena 0: Introdução
            Cena(
                impacto_anterior="Você é um detetive renomado chamado para um caso misterioso.",
                contexto_atual="Você chega à mansão de Lorde Alistair, onde o valioso Diamante Azul foi roubado durante um baile. Há três suspeitos: a governanta Clara, o jardineiro Tom e a sobrinha de Alistair, Lady Eleanor. O mordomo te entrega um bilhete anônimo que diz: 'Procure na biblioteca.'",
                chamada_acao="Por onde você começa?",
                opcoes=[
                    {"texto": "Interrogar a governanta Clara", "correta": True, "consequencia": "Você obtém uma pista inicial.", "proxima_cena": 1},
                    {"texto": "Investigar o jardineiro Tom", "correta": True, "consequencia": "Você encontra vestígios no jardim.", "proxima_cena": 2},
                    {"texto": "Falar com Lady Eleanor", "correta": False, "consequencia": "Ela desvia suas perguntas.", "proxima_cena": 3},
                    {"texto": "Ir direto à biblioteca", "correta": True, "consequencia": "Você descobre um livro suspeito.", "proxima_cena": 4}
                ]
            ),
            # Cena 1: Interrogando Clara
            Cena(
                impacto_anterior="Você interrogou a governanta Clara.",
                contexto_atual="Clara parece nervosa e diz que viu Tom perto do cofre na noite do baile. Ela te dá uma chave que encontrou no corredor, mas não sabe de onde veio.",
                chamada_acao="O que você faz com a chave?",
                opcoes=[
                    {"texto": "Testar a chave no cofre", "correta": True, "consequencia": "A chave abre o cofre vazio.", "proxima_cena": 5},
                    {"texto": "Confrontar Tom com a informação", "correta": True, "consequencia": "Tom reage de forma defensiva.", "proxima_cena": 6},
                    {"texto": "Perguntar a Clara sobre o bilhete", "correta": False, "consequencia": "Ela nega saber de algo.", "proxima_cena": 7}
                ]
            ),
            # Cena 2: Investigando Tom
            Cena(
                impacto_anterior="Você investigou o jardineiro Tom.",
                contexto_atual="No jardim, você acha pegadas frescas perto de uma janela quebrada e uma luva manchada de lama. Tom insiste que estava trabalhando até tarde.",
                chamada_acao="Como você procede?",
                opcoes=[
                    {"texto": "Confrontar Tom com a luva", "correta": True, "consequencia": "Ele hesita e dá uma desculpa.", "proxima_cena": 8},
                    {"texto": "Seguir as pegadas", "correta": True, "consequencia": "Você encontra um esconderijo.", "proxima_cena": 9},
                    {"texto": "Voltar para a mansão", "correta": False, "consequencia": "Você perde uma pista crucial.", "proxima_cena": 10}
                ]
            ),
            # Cena 3: Conversa com Eleanor
            Cena(
                impacto_anterior="Você falou com Lady Eleanor.",
                contexto_atual="Eleanor alega estar doente durante o baile e evita responder sobre sua herança. Ela sugere que Clara pode estar escondendo algo.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Reinterrogar Clara", "correta": True, "consequencia": "Clara fica mais nervosa.", "proxima_cena": 11},
                    {"texto": "Investigar o quarto de Eleanor", "correta": True, "consequencia": "Você acha um diário estranho.", "proxima_cena": 12},
                    {"texto": "Ignorar e seguir em frente", "correta": False, "consequencia": "Você perde tempo.", "proxima_cena": 10}
                ]
            ),
            # Cena 4: Biblioteca
            Cena(
                impacto_anterior="Você foi à biblioteca.",
                contexto_atual="Entre os livros, você encontra um diário escondido com anotações sobre o Diamante Azul. Uma página diz: 'A chave está com quem serve o chá.'",
                chamada_acao="Quem você suspeita?",
                opcoes=[
                    {"texto": "Clara, a governanta", "correta": True, "consequencia": "Você a confronta.", "proxima_cena": 13},
                    {"texto": "Tom, o jardineiro", "correta": False, "consequencia": "Você segue uma pista errada.", "proxima_cena": 14},
                    {"texto": "Eleanor, a sobrinha", "correta": False, "consequencia": "Você perde o foco.", "proxima_cena": 10}
                ]
            ),
            # Cena 5: Cofre Aberto
            Cena(
                impacto_anterior="A chave abriu o cofre.",
                contexto_atual="O cofre está vazio, mas há marcas de arranhões e um pedaço de tecido azul. Clara insiste que não sabe nada.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Analisar o tecido", "correta": True, "consequencia": "Você identifica a origem.", "proxima_cena": 15},
                    {"texto": "Confrontar Clara novamente", "correta": True, "consequencia": "Ela confessa parcialmente.", "proxima_cena": 16},
                    {"texto": "Chamar a polícia", "correta": False, "consequencia": "Você age precipitadamente.", "proxima_cena": 17}
                ]
            ),
            # Cena 6: Confrontando Tom
            Cena(
                impacto_anterior="Você confrontou Tom.",
                contexto_atual="Tom admite que estava no jardim, mas diz que viu Eleanor perto do cofre. Ele te dá uma pista sobre um esconderijo no celeiro.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Investigar o celeiro", "correta": True, "consequencia": "Você acha algo valioso.", "proxima_cena": 18},
                    {"texto": "Confrontar Eleanor", "correta": True, "consequencia": "Ela fica na defensiva.", "proxima_cena": 19},
                    {"texto": "Ignorar Tom", "correta": False, "consequencia": "Você perde uma chance.", "proxima_cena": 10}
                ]
            ),
            # Cena 7: Clara e o Bilhete
            Cena(
                impacto_anterior="Você perguntou a Clara sobre o bilhete.",
                contexto_atual="Clara nega saber do bilhete e sugere que Tom pode estar mentindo. Você sente que ela está escondendo algo.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Investigar Tom", "correta": True, "consequencia": "Você encontra novas pistas.", "proxima_cena": 2},
                    {"texto": "Pressionar Clara", "correta": True, "consequencia": "Ela revela um segredo.", "proxima_cena": 20},
                    {"texto": "Abandonar a pista", "correta": False, "consequencia": "Você perde tempo.", "proxima_cena": 10}
                ]
            ),
            # Cena 8: Confrontando Tom com a Luva
            Cena(
                impacto_anterior="Você confrontou Tom com a luva.",
                contexto_atual="Tom fica pálido e diz que a luva não é dele, mas você nota que ela tem suas iniciais. Ele sugere que Eleanor pode ter plantado evidências.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Investigar Eleanor", "correta": True, "consequencia": "Você acha mais provas.", "proxima_cena": 12},
                    {"texto": "Prender Tom", "correta": False, "consequencia": "Você age cedo demais.", "proxima_cena": 17},
                    {"texto": "Seguir a pista do celeiro", "correta": True, "consequencia": "Você descobre algo.", "proxima_cena": 18}
                ]
            ),
            # Cena 9: Esconderijo no Jardim
            Cena(
                impacto_anterior="Você seguiu as pegadas.",
                contexto_atual="Atrás de um arbusto, você acha um saco com ferramentas de arrombamento e um pedaço do Diamante Azul. Alguém está te observando.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Seguir o observador", "correta": True, "consequencia": "Você encara um suspeito.", "proxima_cena": 21},
                    {"texto": "Voltar com as provas", "correta": True, "consequencia": "Você reúne evidências.", "proxima_cena": 22},
                    {"texto": "Esconder o saco", "correta": False, "consequencia": "Você complica o caso.", "proxima_cena": 10}
                ]
            ),
            # Cena 10: Perda de Tempo (Final Mediano)
            Cena(
                impacto_anterior="Você perdeu uma pista crucial.",
                contexto_atual="Sem progresso significativo, você entrega o caso à polícia, que resolve sem encontrar o diamante. Sua reputação sofre um golpe.",
                chamada_acao="Fim da investigação.",
                opcoes=[]
            ),
            # Cena 11: Reinterrogando Clara
            Cena(
                impacto_anterior="Você reinterrogou Clara.",
                contexto_atual="Clara admite que viu Eleanor mexendo no cofre, mas diz que foi coagida a ficar quieta. Ela te dá um relógio quebrado.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Investigar o relógio", "correta": True, "consequencia": "Você acha uma pista.", "proxima_cena": 23},
                    {"texto": "Confrontar Eleanor", "correta": True, "consequencia": "Ela se defende.", "proxima_cena": 19},
                    {"texto": "Ignorar o relógio", "correta": False, "consequencia": "Você perde tempo.", "proxima_cena": 10}
                ]
            ),
            # Cena 12: Quarto de Eleanor
            Cena(
                impacto_anterior="Você investigou o quarto de Eleanor.",
                contexto_atual="No diário, você lê sobre um plano para roubar o diamante e culpar Clara. Há uma menção a um cofre secreto na adega.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Ir à adega", "correta": True, "consequencia": "Você encontra o cofre.", "proxima_cena": 24},
                    {"texto": "Confrontar Eleanor com o diário", "correta": True, "consequencia": "Ela tenta fugir.", "proxima_cena": 25},
                    {"texto": "Reportar à polícia", "correta": False, "consequencia": "Você age cedo.", "proxima_cena": 17}
                ]
            ),
            # Cena 13: Confrontando Clara com o Bilhete
            Cena(
                impacto_anterior="Você confrontou Clara com o bilhete.",
                contexto_atual="Clara confessa que escreveu o bilhete para desviar suspeitas de si mesma. Ela te leva a um armário secreto.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Abrir o armário", "correta": True, "consequencia": "Você acha o diamante!", "proxima_cena": 26},
                    {"texto": "Prender Clara", "correta": False, "consequencia": "Você erra o alvo.", "proxima_cena": 17},
                    {"texto": "Investigar mais", "correta": True, "consequencia": "Você descobre outro segredo.", "proxima_cena": 27}
                ]
            ),
            # Cena 14: Pista Errada com Tom
            Cena(
                impacto_anterior="Você seguiu uma pista errada sobre Tom.",
                contexto_atual="Você perde tempo investigando Tom, que prova sua inocência com álibis. O caso esfria.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Recomeçar a investigação", "correta": True, "consequencia": "Você volta ao início.", "proxima_cena": 0},
                    {"texto": "Abandonar o caso", "correta": False, "consequencia": "Você falha.", "proxima_cena": 10}
                ]
            ),
            # Cena 15: Análise do Tecido
            Cena(
                impacto_anterior="Você analisou o tecido.",
                contexto_atual="O tecido é de um vestido de Eleanor. Você confronta Clara, que admite tê-lo plantado por ordem de Eleanor.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Confrontar Eleanor", "correta": True, "consequencia": "Ela reage mal.", "proxima_cena": 19},
                    {"texto": "Prender Clara", "correta": False, "consequencia": "Você erra.", "proxima_cena": 17},
                    {"texto": "Seguir a pista de Clara", "correta": True, "consequencia": "Você acha mais provas.", "proxima_cena": 20}
                ]
            ),
            # Cena 16: Clara Confessa Parcialmente
            Cena(
                impacto_anterior="Você confrontou Clara novamente.",
                contexto_atual="Clara admite que ajudou Eleanor, mas diz que foi coagida. Ela te leva a um esconderijo na cozinha.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Verificar o esconderijo", "correta": True, "consequencia": "Você acha uma pista.", "proxima_cena": 28},
                    {"texto": "Prender Clara", "correta": False, "consequencia": "Você erra o plano maior.", "proxima_cena": 17},
                    {"texto": "Confrontar Eleanor", "correta": True, "consequencia": "Ela foge.", "proxima_cena": 25}
                ]
            ),
            # Cena 17: Chamada Prematura à Polícia (Final Ruim)
            Cena(
                impacto_anterior="Você chamou a polícia cedo demais.",
                contexto_atual="A polícia prende o suspeito errado, e o Diamante Azul nunca é encontrado. Sua carreira sofre.",
                chamada_acao="Fim da investigação.",
                opcoes=[]
            ),
            # Cena 18: Celeiro
            Cena(
                impacto_anterior="Você investigou o celeiro.",
                contexto_atual="No celeiro, você acha uma caixa com uma nota: 'O diamante está na adega.' Há pegadas frescas saindo dali.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Seguir as pegadas", "correta": True, "consequencia": "Você encara alguém.", "proxima_cena": 21},
                    {"texto": "Ir à adega", "correta": True, "consequencia": "Você explora o local.", "proxima_cena": 24},
                    {"texto": "Ignorar a nota", "correta": False, "consequencia": "Você perde tempo.", "proxima_cena": 10}
                ]
            ),
            # Cena 19: Confrontando Eleanor
            Cena(
                impacto_anterior="Você confrontou Eleanor.",
                contexto_atual="Eleanor nega tudo e tenta fugir, mas derruba uma bolsa com joias falsas. Ela sugere que Clara é a verdadeira culpada.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Perseguir Eleanor", "correta": True, "consequencia": "Você a captura.", "proxima_cena": 29},
                    {"texto": "Reinterrogar Clara", "correta": True, "consequencia": "Clara cede mais.", "proxima_cena": 20},
                    {"texto": "Ignorar e investigar mais", "correta": False, "consequencia": "Você perde ela.", "proxima_cena": 10}
                ]
            ),
            # Cena 20: Segredo de Clara
            Cena(
                impacto_anterior="Você pressionou Clara ou seguiu sua pista.",
                contexto_atual="Clara confessa que foi paga por Eleanor para distrair o mordomo. Ela te leva a um baú na cozinha.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Abrir o baú", "correta": True, "consequencia": "Você acha o diamante!", "proxima_cena": 26},
                    {"texto": "Confrontar Eleanor", "correta": True, "consequencia": "Ela foge novamente.", "proxima_cena": 25},
                    {"texto": "Prender Clara", "correta": False, "consequencia": "Você erra o plano.", "proxima_cena": 17}
                ]
            ),
            # Cena 21: Seguindo o Observador
            Cena(
                impacto_anterior="Você seguiu o observador.",
                contexto_atual="Você encara Tom, que tenta fugir. Ele joga uma faca, mas você desvia e o encurrala.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Prender Tom", "correta": False, "consequencia": "Você erra o culpado.", "proxima_cena": 17},
                    {"texto": "Interrogá-lo", "correta": True, "consequencia": "Ele revela uma pista.", "proxima_cena": 30},
                    {"texto": "Deixá-lo ir", "correta": False, "consequencia": "Você perde a chance.", "proxima_cena": 10}
                ]
            ),
            # Cena 22: Provas Reunidas
            Cena(
                impacto_anterior="Você voltou com as provas.",
                contexto_atual="Com o saco de ferramentas, você confronta Clara, que admite ter sido coagida por Eleanor. Ela te leva à adega.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Ir à adega", "correta": True, "consequencia": "Você encontra o cofre.", "proxima_cena": 24},
                    {"texto": "Prender Clara", "correta": False, "consequencia": "Você falha.", "proxima_cena": 17},
                    {"texto": "Confrontar Eleanor", "correta": True, "consequencia": "Ela foge.", "proxima_cena": 25}
                ]
            ),
            # Cena 23: Investigando o Relógio
            Cena(
                impacto_anterior="Você investigou o relógio.",
                contexto_atual="Dentro do relógio, há uma nota com as iniciais 'E.A.' (Eleanor Alistair) e uma menção à adega. Uma pista valiosa!",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Ir à adega", "correta": True, "consequencia": "Você explora o local.", "proxima_cena": 24},
                    {"texto": "Confrontar Eleanor", "correta": True, "consequencia": "Ela reage.", "proxima_cena": 19},
                    {"texto": "Ignorar a nota", "correta": False, "consequencia": "Você perde tempo.", "proxima_cena": 10}
                ]
            ),
            # Cena 24: Adega
            Cena(
                impacto_anterior="Você foi à adega.",
                contexto_atual="Na adega, você acha um cofre trancado com uma fechadura complexa. Há marcas de arranhões recentes.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Tentar abrir com a chave de Clara", "correta": True, "consequencia": "Você acha o diamante!", "proxima_cena": 26},
                    {"texto": "Forçar o cofre", "correta": False, "consequencia": "Você danifica as provas.", "proxima_cena": 17},
                    {"texto": "Chamar reforços", "correta": True, "consequencia": "Você resolve o caso.", "proxima_cena": 31}
                ]
            ),
            # Cena 25: Eleanor Fugindo
            Cena(
                impacto_anterior="Eleanor tentou fugir.",
                contexto_atual="Você a persegue até o jardim, onde ela tropeça e deixa cair uma bolsa com o Diamante Azul. Ela implora por clemência.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Prendê-la", "correta": True, "consequencia": "Você resolve o caso.", "proxima_cena": 32},
                    {"texto": "Deixá-la ir", "correta": False, "consequencia": "Ela escapa.", "proxima_cena": 10},
                    {"texto": "Questioná-la", "correta": True, "consequencia": "Ela confessa.", "proxima_cena": 33}
                ]
            ),
            # Cena 26: Diamante Encontrado
            Cena(
                impacto_anterior="Você abriu o armário ou cofre.",
                contexto_atual="O Diamante Azul brilha em suas mãos. Você ouve passos se aproximando — Eleanor aparece, furiosa.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Confrontá-la", "correta": True, "consequencia": "Ela confessa.", "proxima_cena": 33},
                    {"texto": "Esconder o diamante", "correta": False, "consequencia": "Ela te ataca.", "proxima_cena": 17},
                    {"texto": "Chamar a polícia", "correta": True, "consequencia": "Você fecha o caso.", "proxima_cena": 32}
                ]
            ),
            # Cena 27: Outro Segredo
            Cena(
                impacto_anterior="Você investigou mais após o armário.",
                contexto_atual="No armário, além do diamante, você acha cartas que implicam Tom como cúmplice de Eleanor. Uma trama maior se revela.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Confrontar Tom", "correta": True, "consequencia": "Ele confessa.", "proxima_cena": 34},
                    {"texto": "Prender Eleanor", "correta": True, "consequencia": "Você resolve parcialmente.", "proxima_cena": 32},
                    {"texto": "Ignorar as cartas", "correta": False, "consequencia": "Você falha.", "proxima_cena": 10}
                ]
            ),
            # Cena 28: Esconderijo na Cozinha
            Cena(
                impacto_anterior="Você verificou o esconderijo na cozinha.",
                contexto_atual="No baú, você acha o Diamante Azul envolto em um pano. Clara aparece, tentando explicar.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Prender Clara", "correta": False, "consequencia": "Você erra.", "proxima_cena": 17},
                    {"texto": "Confrontar Eleanor", "correta": True, "consequencia": "Ela foge.", "proxima_cena": 25},
                    {"texto": "Ouvir Clara", "correta": True, "consequencia": "Ela revela tudo.", "proxima_cena": 35}
                ]
            ),
            # Cena 29: Capturando Eleanor
            Cena(
                impacto_anterior="Você perseguiu Eleanor.",
                contexto_atual="Você a pega no jardim e encontra o Diamante Azul em sua bolsa. Ela chora e implora por perdão.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Prendê-la", "correta": True, "consequencia": "Caso resolvido.", "proxima_cena": 32},
                    {"texto": "Deixá-la ir", "correta": False, "consequencia": "Ela escapa.", "proxima_cena": 10},
                    {"texto": "Questioná-la", "correta": True, "consequencia": "Ela confessa.", "proxima_cena": 33}
                ]
            ),
            # Cena 30: Interrogando Tom
            Cena(
                impacto_anterior="Você interrogou Tom.",
                contexto_atual="Tom admite que ajudou Eleanor por dinheiro, mas diz que ela planejou tudo. Ele te leva à adega.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Ir à adega", "correta": True, "consequencia": "Você acha o cofre.", "proxima_cena": 24},
                    {"texto": "Prender Tom", "correta": False, "consequencia": "Você falha.", "proxima_cena": 17},
                    {"texto": "Confrontar Eleanor", "correta": True, "consequencia": "Ela foge.", "proxima_cena": 25}
                ]
            ),
            # Cena 31: Reforços na Adega
            Cena(
                impacto_anterior="Você chamou reforços.",
                contexto_atual="A polícia chega e abre o cofre com ferramentas. O Diamante Azul é recuperado, e Eleanor é presa com base nas provas.",
                chamada_acao="Fim da investigação.",
                opcoes=[]
            ),
            # Cena 32: Caso Resolvido (Final Bom)
            Cena(
                impacto_anterior="Você prendeu Eleanor ou chamou a polícia.",
                contexto_atual="O Diamante Azul é devolvido a Lorde Alistair, e sua reputação como detetive sobe. Eleanor é condenada, mas o caso deixa dúvidas sobre cúmplices.",
                chamada_acao="Fim da investigação.",
                opcoes=[]
            ),
            # Cena 33: Confissão de Eleanor
            Cena(
                impacto_anterior="Você questionou Eleanor.",
                contexto_atual="Eleanor confessa que planejou o roubo para pagar dívidas, usando Clara e Tom. Ela te leva ao diamante escondido.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Recuperar o diamante", "correta": True, "consequencia": "Caso fechado.", "proxima_cena": 32},
                    {"texto": "Prendê-la imediatamente", "correta": True, "consequencia": "Caso resolvido.", "proxima_cena": 32},
                    {"texto": "Deixá-la ir", "correta": False, "consequencia": "Ela escapa.", "proxima_cena": 10}
                ]
            ),
            # Cena 34: Confissão de Tom
            Cena(
                impacto_anterior="Você confrontou Tom.",
                contexto_atual="Tom confessa que foi pago por Eleanor para abrir o cofre. Ele te leva a um esconderijo na adega com o diamante.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Recuperar o diamante", "correta": True, "consequencia": "Caso fechado.", "proxima_cena": 32},
                    {"texto": "Prender Tom", "correta": True, "consequencia": "Caso resolvido.", "proxima_cena": 32},
                    {"texto": "Ignorar", "correta": False, "consequencia": "Você falha.", "proxima_cena": 10}
                ]
            ),
            # Cena 35: Clara Revela Tudo
            Cena(
                impacto_anterior="Você ouviu Clara.",
                contexto_atual="Clara confessa que foi coagida por Eleanor a esconder o diamante. Ela te leva ao baú na cozinha, onde o diamante está.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Recuperar o diamante", "correta": True, "consequencia": "Caso fechado.", "proxima_cena": 32},
                    {"texto": "Prender Clara", "correta": False, "consequencia": "Você erra.", "proxima_cena": 17},
                    {"texto": "Confrontar Eleanor", "correta": True, "consequencia": "Ela confessa.", "proxima_cena": 33}
                ]
            )
        ]
        return cenas

    def processar_escolha(self, escolha):
        """Processa a escolha do jogador e atualiza o estado."""
        if self.cena_atual >= len(self.cenas):
            return "Fim da investigação", False, None
        
        consequencia, correta, proxima_cena = self.cenas[self.cena_atual].processar_escolha(escolha)
        print(f"Processando escolha: Cena atual {self.cena_atual}, Próxima cena {proxima_cena}, Correta: {correta}")
        if proxima_cena is not None:
            self.cena_atual = proxima_cena
            self.pontuacao += 10 if correta else -5
            print(f"Atualizado: Cena {self.cena_atual}, Pontuação {self.pontuacao}")
        if self.cenas[self.cena_atual].opcoes == []:  # Verifica se é uma cena final
            self.cena_atual = len(self.cenas)  # Força o fim
            print(f"Detectado fim na cena {self.cena_atual}")
        return consequencia, correta, proxima_cena

    def to_dict(self):
        """Serializa a história para a sessão."""
        return {
            "nome": self.nome,
            "linear": self.linear,
            "cenas": [c.__dict__ for c in self.cenas],
            "cena_atual": self.cena_atual,
            "pontuacao": self.pontuacao
        }

    @classmethod
    def from_dict(cls, data):
        """Desserializa a história a partir de um dicionário."""
        historia = cls()
        historia.nome = data["nome"]
        historia.linear = data["linear"]
        historia.cena_atual = data["cena_atual"]
        historia.pontuacao = data["pontuacao"]
        historia.cenas = [Cena(**c) for c in data["cenas"]]
        return historia