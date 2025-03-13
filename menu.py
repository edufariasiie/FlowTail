# menu.py
"""
Define a classe Menu para o FlowTale, que gerencia as histórias disponíveis.
"""

class Menu:
    def __init__(self):
        """
        Inicializa o menu do FlowTale.
        Atributos:
            historias (dict): Dicionário {nome: classe} das histórias.
        """
        self.historias = {}

    def adicionar_historia(self, nome, classe):
        """
        Adiciona uma história ao menu do FlowTale.
        Parâmetros:
            nome (str): Nome da história.
            classe (class): Classe da história (ex.: Historia).
        """
        self.historias[nome] = classe