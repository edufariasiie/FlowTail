# historia_medieval.py
"""
Define a história medieval fantástica 'A Lenda do Coração de Dragão' para o FlowTale.
História não linear com escolhas que levam a diferentes finais.
"""

from cena import Cena

class HistoriaMedieval:
    def __init__(self):
        self.nome = "A Lenda do Coração de Dragão"
        self.linear = False
        self.cenas = self.inicializar_cenas()
        self.cena_atual = 0
        self.pontuacao = 0

    def inicializar_cenas(self):
        """Inicializa as cenas da aventura medieval."""
        cenas = [
            # Cena 0: Introdução
            Cena(
                impacto_anterior="Você é um jovem aventureiro em busca de fama.",
                contexto_atual="Você está em uma vila nas bordas do Reino de Eldoria. Rumores falam de um dragão antigo que guarda o Coração de Dragão, uma joia mágica que concede poder ilimitado. A vila está em polvorosa: o ferreiro foi capturado por goblins nas montanhas, e o líder local pede ajuda.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Oferecer-se para resgatar o ferreiro", "correta": True, "consequencia": "Você parte para as montanhas.", "proxima_cena": 1},
                    {"texto": "Ignorar e ir direto ao covil do dragão", "correta": False, "consequencia": "Você segue sozinho para o desconhecido.", "proxima_cena": 2},
                    {"texto": "Pedir mais informações ao líder", "correta": True, "consequencia": "Você descobre pistas valiosas.", "proxima_cena": 3}
                ]
            ),
            # Cena 1: Resgate nas Montanhas
            Cena(
                impacto_anterior="Você decidiu resgatar o ferreiro.",
                contexto_atual="Nas montanhas, você encontra um acampamento goblin. O ferreiro está preso em uma jaula de madeira, vigiado por dois goblins armados com lanças enferrujadas. Há um caminho estreito à esquerda e uma ravina à direita.",
                chamada_acao="Como você procede?",
                opcoes=[
                    {"texto": "Atacar os goblins diretamente", "correta": False, "consequencia": "Você luta, mas é ferido.", "proxima_cena": 4},
                    {"texto": "Usar o caminho estreito para se esgueirar", "correta": True, "consequencia": "Você se aproxima furtivamente.", "proxima_cena": 5},
                    {"texto": "Causar uma distração na ravina", "correta": True, "consequencia": "Os goblins se afastam da jaula.", "proxima_cena": 6}
                ]
            ),
            # Cena 2: Covil do Dragão (Caminho Direto)
            Cena(
                impacto_anterior="Você ignorou a vila e foi ao covil do dragão.",
                contexto_atual="Você chega ao sopé de uma montanha fumegante. A entrada do covil é uma caverna escura, exalando calor. Sem aliados ou informações, você ouve um rugido distante.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Entrar na caverna imediatamente", "correta": False, "consequencia": "Você enfrenta o dragão despreparado.", "proxima_cena": 7},
                    {"texto": "Explorar os arredores primeiro", "correta": True, "consequencia": "Você encontra uma lança mágica abandonada.", "proxima_cena": 8}
                ]
            ),
            # Cena 3: Informações do Líder
            Cena(
                impacto_anterior="Você pediu mais informações ao líder.",
                contexto_atual="O líder revela que o ferreiro sabe o segredo para enfraquecer o dragão: uma erva rara chamada Flor de Cinzas, que cresce nas montanhas. Ele te dá um mapa parcial.",
                chamada_acao="Qual é seu próximo passo?",
                opcoes=[
                    {"texto": "Ir atrás do ferreiro nas montanhas", "correta": True, "consequencia": "Você segue o mapa.", "proxima_cena": 1},
                    {"texto": "Procurar a Flor de Cinzas sozinho", "correta": True, "consequencia": "Você parte em busca da erva.", "proxima_cena": 9}
                ]
            ),
            # Cena 4: Luta Direta com Goblins
            Cena(
                impacto_anterior="Você atacou os goblins diretamente.",
                contexto_atual="A batalha é feroz. Você derrota os goblins, mas leva uma lança no ombro. O ferreiro, grato, te dá uma espada reforçada antes de fugir de volta à vila.",
                chamada_acao="O que você faz agora?",
                opcoes=[
                    {"texto": "Seguir para o covil do dragão", "correta": True, "consequencia": "Você avança ferido, mas armado.", "proxima_cena": 10},
                    {"texto": "Voltar à vila para se curar", "correta": False, "consequencia": "Você perde tempo precioso.", "proxima_cena": 11}
                ]
            ),
            # Cena 5: Furtividade Bem-Sucedida
            Cena(
                impacto_anterior="Você se esgueirou pelo caminho estreito.",
                contexto_atual="Você chega perto da jaula sem ser visto. O ferreiro sussurra que conhece o segredo do dragão e te entrega um frasco com pó de Flor de Cinzas antes de escapar.",
                chamada_acao="Qual é seu próximo movimento?",
                opcoes=[
                    {"texto": "Ir ao covil do dragão com o pó", "correta": True, "consequencia": "Você segue preparado.", "proxima_cena": 12},
                    {"texto": "Voltar à vila com o ferreiro", "correta": False, "consequencia": "Você hesita na missão.", "proxima_cena": 11}
                ]
            ),
            # Cena 6: Distração na Ravina
            Cena(
                impacto_anterior="Você causou uma distração na ravina.",
                contexto_atual="Os goblins correm para investigar o barulho. Você liberta o ferreiro, que te agradece com uma adaga encantada e diz que a Flor de Cinzas enfraquece o dragão.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Procurar a Flor de Cinzas", "correta": True, "consequencia": "Você segue a dica do ferreiro.", "proxima_cena": 9},
                    {"texto": "Ir direto ao covil do dragão", "correta": True, "consequencia": "Você avança com a adaga.", "proxima_cena": 10}
                ]
            ),
            # Cena 7: Dragão Despreparado (Final Ruim)
            Cena(
                impacto_anterior="Você entrou na caverna sem preparo.",
                contexto_atual="O dragão te encara, suas escamas brilhando como aço. Sem armas ou aliados, você é incinerado em segundos.",
                chamada_acao="Fim da aventura.",
                opcoes=[]
            ),
            # Cena 8: Lança Mágica
            Cena(
                impacto_anterior="Você explorou os arredores da caverna.",
                contexto_atual="Você encontra uma lança cravada em uma pedra, pulsando com energia mágica. Ao pegá-la, sente um poder crescente. O rugido do dragão ecoa mais perto.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Entrar na caverna com a lança", "correta": True, "consequencia": "Você enfrenta o dragão armado.", "proxima_cena": 13}
                ]
            ),
            # Cena 9: Busca pela Flor de Cinzas
            Cena(
                impacto_anterior="Você decidiu procurar a Flor de Cinzas.",
                contexto_atual="Nas encostas das montanhas, você acha a erva rara entre rochas fumegantes. Seu aroma é acre, mas poderoso. O covil do dragão não está longe.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Ir ao covil com a Flor de Cinzas", "correta": True, "consequencia": "Você está pronto para o confronto.", "proxima_cena": 12}
                ]
            ),
            # Cena 10: Covil com Adaga ou Espada
            Cena(
                impacto_anterior="Você chegou ao covil com uma arma.",
                contexto_atual="O dragão te encara, mas sua arma dá uma chance. Ele ataca com fogo, mas você esquiva. Sem a Flor de Cinzas, a luta é brutal.",
                chamada_acao="Como você luta?",
                opcoes=[
                    {"texto": "Atacar diretamente", "correta": False, "consequencia": "Você fere o dragão, mas morre no fogo.", "proxima_cena": 14},
                    {"texto": "Esperar uma abertura", "correta": True, "consequencia": "Você derrota o dragão com esforço.", "proxima_cena": 15}
                ]
            ),
            # Cena 11: Retorno à Vila (Final Mediano)
            Cena(
                impacto_anterior="Você voltou à vila.",
                contexto_atual="Os aldeões te recebem como herói por salvar o ferreiro, mas o dragão continua a ameaçar Eldoria. Sua jornada termina sem glória.",
                chamada_acao="Fim da aventura.",
                opcoes=[]
            ),
            # Cena 12: Covil com Flor de Cinzas
            Cena(
                impacto_anterior="Você entrou no covil com a Flor de Cinzas.",
                contexto_atual="Você joga o pó no ar, e o dragão enfraquece, tossindo. Suas escamas perdem o brilho. É sua chance de atacar!",
                chamada_acao="Como você termina isso?",
                opcoes=[
                    {"texto": "Golpear o coração do dragão", "correta": True, "consequencia": "Você reivindica a joia.", "proxima_cena": 16},
                    {"texto": "Tentar negociar com o dragão", "correta": False, "consequencia": "O dragão te engana e ataca.", "proxima_cena": 14}
                ]
            ),
            # Cena 13: Covil com Lança Mágica
            Cena(
                impacto_anterior="Você entrou com a lança mágica.",
                contexto_atual="O dragão cospe fogo, mas a lança absorve o calor. Você avança, sentindo a magia te guiar até o coração da besta.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Arremessar a lança no coração", "correta": True, "consequencia": "Você derrota o dragão.", "proxima_cena": 16}
                ]
            ),
            # Cena 14: Final Ruim (Morte)
            Cena(
                impacto_anterior="Você falhou contra o dragão.",
                contexto_atual="O dragão te engole em chamas. Sua aventura termina em cinzas.",
                chamada_acao="Fim da aventura.",
                opcoes=[]
            ),
            # Cena 15: Final Bom (Sem Joia)
            Cena(
                impacto_anterior="Você esperou uma abertura e venceu.",
                contexto_atual="O dragão cai, exausto. Você sobrevive, mas o Coração de Dragão está quebrado na luta. Eldoria está segura, mas sem recompensa mágica.",
                chamada_acao="Fim da aventura.",
                opcoes=[]
            ),
            # Cena 16: Final Épico
            Cena(
                impacto_anterior="Você golpeou o coração do dragão.",
                contexto_atual="O dragão ruge uma última vez antes de colapsar. O Coração de Dragão brilha em suas mãos, pulsando com poder. Você é a lenda de Eldoria!",
                chamada_acao="Fim da aventura.",
                opcoes=[]
            )
        ]
        return cenas

    def processar_escolha(self, escolha):
        """Processa a escolha do jogador e atualiza o estado."""
        if self.cena_atual >= len(self.cenas):
            return "Fim da história", False, None
        
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