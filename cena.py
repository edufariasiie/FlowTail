# cena.py
"""
Define a classe Cena para o FlowTale, representando uma cena interativa.
Suporta histórias lineares (progressão sequencial) e não lineares (destinos definidos por escolhas).
"""

class Cena:
    def __init__(self, impacto_anterior, contexto_atual, chamada_acao, opcoes, pontos=None):
        """
        Inicializa uma cena do FlowTale.
        Parâmetros:
            impacto_anterior (str): Consequências da escolha anterior.
            contexto_atual (str): Descrição do cenário atual.
            chamada_acao (str): Desafio apresentado ao jogador.
            opcoes (list): Lista de dicionários {texto, correta, consequencia, proxima_cena}.
            pontos (int, opcional): Pontuação da cena (default calculado se None).
        Atributos:
            impacto_anterior (str): Contexto passado.
            contexto_atual (str): Cenário atual.
            chamada_acao (str): Desafio atual.
            opcoes (list): Opções disponíveis.
            pontos (int): Pontuação da cena (10 se correta, -5 se errada, ou valor fornecido).
        """
        self.impacto_anterior = impacto_anterior
        self.contexto_atual = contexto_atual
        self.chamada_acao = chamada_acao
        self.opcoes = opcoes
        # Usa o valor fornecido para pontos, ou calcula se for None
        self.pontos = pontos if pontos is not None else (10 if any(op["correta"] for op in opcoes) else -5)

    def processar_escolha(self, escolha):
        """
        Processa a escolha do jogador no FlowTale.
        Parâmetros:
            escolha (int): Índice da opção escolhida.
        Retorna:
            Tuple (consequência: str, correta: bool, proxima_cena: int/None).
        """
        if 0 <= escolha < len(self.opcoes):
            opcao = self.opcoes[escolha]
            return opcao["consequencia"], opcao["correta"], opcao.get("proxima_cena")
        return "Escolha inválida no FlowTale", False, None

    def __repr__(self):
        """Representação da cena para depuração."""
        return f"Cena(impacto_anterior='{self.impacto_anterior}', contexto_atual='{self.contexto_atual}', chamada_acao='{self.chamada_acao}', opcoes={self.opcoes}, pontos={self.pontos})"