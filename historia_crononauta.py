# historia_crononauta.py
"""
Define a história de ficção científica 'Paradoxo do Crononauta' para o FlowTale.
História não linear com escolhas que afetam o fluxo do tempo e levam a diferentes finais.
"""

from cena import Cena

class HistoriaCrononauta:
    def __init__(self):
        self.nome = "Paradoxo do Crononauta"
        self.linear = False
        self.cenas = self.inicializar_cenas()
        self.cena_atual = 0
        self.pontuacao = 0

    def inicializar_cenas(self):
        """Inicializa as cenas da aventura de viagem no tempo."""
        cenas = [
            # Cena 0: Introdução
            Cena(
                impacto_anterior="Você é um crononauta do ano 2147, treinado para consertar falhas temporais.",
                contexto_atual="Sua missão é impedir o 'Incidente Zero', um evento em 1945 que causou o colapso do futuro. Você ativa seu Crono-Dispositivo e viaja até 1945, chegando a uma base militar secreta. Um cientista chamado Dr. Hans te recebe, mas você percebe que há um agente da Ordem do Tempo (uma organização que controla o fluxo temporal) infiltrado na base.",
                chamada_acao="Por onde você começa?",
                opcoes=[
                    {"texto": "Interrogar Dr. Hans sobre o Incidente Zero", "correta": True, "consequencia": "Você obtém informações cruciais.", "proxima_cena": 1},
                    {"texto": "Procurar o agente da Ordem do Tempo", "correta": True, "consequencia": "Você encontra pistas suspeitas.", "proxima_cena": 2},
                    {"texto": "Sabotar o projeto da base", "correta": False, "consequencia": "Você age sem informações.", "proxima_cena": 3},
                    {"texto": "Viajar para outro ponto no tempo", "correta": False, "consequencia": "Você perde o foco inicial.", "proxima_cena": 4}
                ]
            ),
            # Cena 1: Interrogando Dr. Hans
            Cena(
                impacto_anterior="Você interrogou Dr. Hans.",
                contexto_atual="Dr. Hans revela que o Incidente Zero foi causado por uma explosão de um reator temporal experimental. Ele menciona uma assistente, Clara, que desapareceu com documentos cruciais. Você nota que ele está escondendo algo.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Pressionar Dr. Hans por mais detalhes", "correta": True, "consequencia": "Ele revela um segredo.", "proxima_cena": 5},
                    {"texto": "Procurar pistas sobre Clara", "correta": True, "consequencia": "Você acha uma pista dela.", "proxima_cena": 6},
                    {"texto": "Ignorar e sabotar o reator", "correta": False, "consequencia": "Você age sem preparo.", "proxima_cena": 7}
                ]
            ),
            # Cena 2: Procurando o Agente
            Cena(
                impacto_anterior="Você procurou o agente da Ordem do Tempo.",
                contexto_atual="Nos arquivos da base, você encontra um rádio codificado enviando mensagens para a Ordem do Tempo. Um soldado chamado Viktor entra e te confronta, suspeitando de você.",
                chamada_acao="Como você reage?",
                opcoes=[
                    {"texto": "Convencer Viktor que você é aliado", "correta": True, "consequencia": "Ele te ajuda.", "proxima_cena": 8},
                    {"texto": "Desarmar Viktor e fugir", "correta": False, "consequencia": "Você levanta suspeitas.", "proxima_cena": 9},
                    {"texto": "Usar o Crono-Dispositivo pra fugir", "correta": False, "consequencia": "Você viaja sem pistas.", "proxima_cena": 4}
                ]
            ),
            # Cena 3: Sabotagem Direta
            Cena(
                impacto_anterior="Você sabotou o projeto da base sem informações.",
                contexto_atual="Você desativa o reator, mas isso cria um paradoxo temporal. O futuro colapsa ainda mais, e você é apagado da existência.",
                chamada_acao="Fim da missão.",
                opcoes=[]
            ),
            # Cena 4: Viagem no Tempo Precoce
            Cena(
                impacto_anterior="Você viajou para outro ponto no tempo sem informações.",
                contexto_atual="Você chega ao ano 2077, mas sem contexto, é capturado pela Ordem do Tempo, que te interroga e desativa seu Crono-Dispositivo.",
                chamada_acao="Fim da missão.",
                opcoes=[]
            ),
            # Cena 5: Pressionando Dr. Hans
            Cena(
                impacto_anterior="Você pressionou Dr. Hans.",
                contexto_atual="Dr. Hans confessa que Clara era uma agente da Ordem do Tempo infiltrada. Ele te dá um código para acessar o laboratório secreto onde o reator está.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Ir ao laboratório secreto", "correta": True, "consequencia": "Você acessa o reator.", "proxima_cena": 10},
                    {"texto": "Procurar Clara", "correta": True, "consequencia": "Você segue sua pista.", "proxima_cena": 6},
                    {"texto": "Sabotar o reator agora", "correta": False, "consequencia": "Você age cedo demais.", "proxima_cena": 7}
                ]
            ),
            # Cena 6: Pista sobre Clara
            Cena(
                impacto_anterior="Você procurou pistas sobre Clara.",
                contexto_atual="Nos aposentos dela, você acha um bilhete codificado: 'Encontro na ponte às 22h.' Você também encontra um dispositivo da Ordem do Tempo.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Ir à ponte às 22h", "correta": True, "consequencia": "Você intercepta Clara.", "proxima_cena": 11},
                    {"texto": "Analisar o dispositivo", "correta": True, "consequencia": "Você descobre um plano.", "proxima_cena": 12},
                    {"texto": "Voltar e falar com Dr. Hans", "correta": False, "consequencia": "Você perde tempo.", "proxima_cena": 13}
                ]
            ),
            # Cena 7: Sabotagem Precoce
            Cena(
                impacto_anterior="Você sabotou o reator sem preparo.",
                contexto_atual="O reator explode, criando um paradoxo. Você é apagado da linha do tempo, e o futuro é destruído.",
                chamada_acao="Fim da missão.",
                opcoes=[]
            ),
            # Cena 8: Aliando-se a Viktor
            Cena(
                impacto_anterior="Você convenceu Viktor.",
                contexto_atual="Viktor te ajuda a rastrear o agente. Ele te leva ao laboratório secreto, onde você vê o reator temporal e um dispositivo da Ordem do Tempo.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Analisar o dispositivo", "correta": True, "consequencia": "Você descobre um plano.", "proxima_cena": 12},
                    {"texto": "Desativar o reator", "correta": True, "consequencia": "Você tenta impedir o incidente.", "proxima_cena": 14},
                    {"texto": "Procurar Clara", "correta": True, "consequencia": "Você segue a pista.", "proxima_cena": 6}
                ]
            ),
            # Cena 9: Fuga de Viktor
            Cena(
                impacto_anterior="Você desarmou Viktor e fugiu.",
                contexto_atual="A base entra em alerta, e você é caçado. Sem aliados, você é capturado pela Ordem do Tempo.",
                chamada_acao="Fim da missão.",
                opcoes=[]
            ),
            # Cena 10: Laboratório Secreto
            Cena(
                impacto_anterior="Você acessou o laboratório secreto.",
                contexto_atual="O reator temporal está ativo, pulsando com energia. Você encontra documentos que indicam que o Incidente Zero será hoje à noite, às 23h.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Desativar o reator agora", "correta": True, "consequencia": "Você tenta impedir o incidente.", "proxima_cena": 14},
                    {"texto": "Esperar até 23h para agir", "correta": True, "consequencia": "Você planeja melhor.", "proxima_cena": 15},
                    {"texto": "Procurar Clara", "correta": True, "consequencia": "Você busca mais informações.", "proxima_cena": 6}
                ]
            ),
            # Cena 11: Encontro na Ponte
            Cena(
                impacto_anterior="Você foi à ponte às 22h.",
                contexto_atual="Você vê Clara conversando com um agente da Ordem do Tempo. Eles mencionam um plano para acelerar o Incidente Zero. Clara te vê e foge.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Perseguir Clara", "correta": True, "consequencia": "Você a captura.", "proxima_cena": 16},
                    {"texto": "Seguir o agente", "correta": True, "consequencia": "Você descobre mais.", "proxima_cena": 17},
                    {"texto": "Voltar ao laboratório", "correta": False, "consequencia": "Você perde a pista.", "proxima_cena": 10}
                ]
            ),
            # Cena 12: Analisando o Dispositivo
            Cena(
                impacto_anterior="Você analisou o dispositivo da Ordem.",
                contexto_atual="O dispositivo revela que a Ordem do Tempo planeja usar o Incidente Zero para destruir a resistência do futuro. Há coordenadas para 2077.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Viajar para 2077", "correta": True, "consequencia": "Você enfrenta a Ordem.", "proxima_cena": 18},
                    {"texto": "Desativar o reator agora", "correta": True, "consequencia": "Você impede o incidente.", "proxima_cena": 14},
                    {"texto": "Procurar Clara", "correta": True, "consequencia": "Você busca mais pistas.", "proxima_cena": 6}
                ]
            ),
            # Cena 13: Perda de Tempo com Dr. Hans
            Cena(
                impacto_anterior="Você voltou para falar com Dr. Hans.",
                contexto_atual="Dr. Hans te dá informações repetidas, e você perde tempo. A Ordem do Tempo ativa o reator antes que você possa agir.",
                chamada_acao="Fim da missão.",
                opcoes=[]
            ),
            # Cena 14: Desativando o Reator
            Cena(
                impacto_anterior="Você tentou desativar o reator.",
                contexto_atual="Você desativa o reator, mas sem conhecer os detalhes, cria um pequeno paradoxo. O futuro muda, mas você sobrevive com danos ao Crono-Dispositivo.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Reparar o Crono-Dispositivo", "correta": True, "consequencia": "Você tenta consertar.", "proxima_cena": 19},
                    {"texto": "Viajar para 2077 mesmo assim", "correta": True, "consequencia": "Você enfrenta a Ordem.", "proxima_cena": 18},
                    {"texto": "Ficar em 1945", "correta": False, "consequencia": "Você desiste da missão.", "proxima_cena": 20}
                ]
            ),
            # Cena 15: Esperando até 23h
            Cena(
                impacto_anterior="Você esperou até 23h para agir.",
                contexto_atual="Às 23h, você vê Clara ativando o reator. Ela está com o agente da Ordem do Tempo, e o reator começa a sobrecarregar.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Confrontar Clara", "correta": True, "consequencia": "Você tenta detê-la.", "proxima_cena": 16},
                    {"texto": "Atacar o agente", "correta": True, "consequencia": "Você enfrenta a Ordem.", "proxima_cena": 21},
                    {"texto": "Desativar o reator", "correta": True, "consequencia": "Você age diretamente.", "proxima_cena": 14}
                ]
            ),
            # Cena 16: Capturando Clara
            Cena(
                impacto_anterior="Você perseguiu e capturou Clara.",
                contexto_atual="Clara confessa que foi forçada pela Ordem do Tempo a sabotar o reator. Ela te dá um código para desativá-lo.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Usar o código no reator", "correta": True, "consequencia": "Você tenta impedir o incidente.", "proxima_cena": 22},
                    {"texto": "Interrogar Clara mais", "correta": True, "consequencia": "Ela revela mais.", "proxima_cena": 23},
                    {"texto": "Deixar Clara e ir embora", "correta": False, "consequencia": "Você falha.", "proxima_cena": 13}
                ]
            ),
            # Cena 17: Seguindo o Agente
            Cena(
                impacto_anterior="Você seguiu o agente da Ordem.",
                contexto_atual="O agente te leva a um esconderijo, onde você descobre que a Ordem planeja viajar a 2077 para consolidar o poder.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Viajar para 2077", "correta": True, "consequencia": "Você enfrenta a Ordem.", "proxima_cena": 18},
                    {"texto": "Voltar e desativar o reator", "correta": True, "consequencia": "Você impede o incidente.", "proxima_cena": 14},
                    {"texto": "Capturar o agente", "correta": True, "consequencia": "Você ganha informações.", "proxima_cena": 24}
                ]
            ),
            # Cena 18: Viagem para 2077
            Cena(
                impacto_anterior="Você viajou para 2077.",
                contexto_atual="Você chega a uma cidade futurista controlada pela Ordem do Tempo. Um líder da resistência, Ana, te encontra e pede ajuda para destruir a Ordem.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Juntar-se à resistência", "correta": True, "consequencia": "Você planeja um ataque.", "proxima_cena": 25},
                    {"texto": "Atacar a Ordem sozinho", "correta": False, "consequencia": "Você é capturado.", "proxima_cena": 4},
                    {"texto": "Tentar negociar com a Ordem", "correta": True, "consequencia": "Você busca um acordo.", "proxima_cena": 26}
                ]
            ),
            # Cena 19: Reparando o Crono-Dispositivo
            Cena(
                impacto_anterior="Você tentou reparar o Crono-Dispositivo.",
                contexto_atual="Com ferramentas da base, você conserta o dispositivo, mas ele só tem energia para uma viagem. Você sente que o tempo está se esgotando.",
                chamada_acao="Para onde você vai?",
                opcoes=[
                    {"texto": "Voltar para 2147", "correta": True, "consequencia": "Você retorna ao futuro.", "proxima_cena": 27},
                    {"texto": "Ir para 2077", "correta": True, "consequencia": "Você enfrenta a Ordem.", "proxima_cena": 18},
                    {"texto": "Ficar em 1945", "correta": False, "consequencia": "Você desiste.", "proxima_cena": 20}
                ]
            ),
            # Cena 20: Desistência em 1945 (Final Mediano)
            Cena(
                impacto_anterior="Você decidiu ficar em 1945.",
                contexto_atual="Você abandona a missão e vive uma vida tranquila em 1945, mas o futuro colapsa sem sua intervenção. Sua história termina em silêncio.",
                chamada_acao="Fim da missão.",
                opcoes=[]
            ),
            # Cena 21: Atacando o Agente
            Cena(
                impacto_anterior="Você atacou o agente da Ordem.",
                contexto_atual="Você desarma o agente, mas ele ativa um dispositivo de autodestruição. Você tem poucos segundos para agir.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Desativar o dispositivo", "correta": True, "consequencia": "Você sobrevive.", "proxima_cena": 24},
                    {"texto": "Fugir com o Crono-Dispositivo", "correta": True, "consequencia": "Você viaja no tempo.", "proxima_cena": 18},
                    {"texto": "Tentar salvar Clara", "correta": False, "consequencia": "Você é pego na explosão.", "proxima_cena": 7}
                ]
            ),
            # Cena 22: Usando o Código no Reator
            Cena(
                impacto_anterior="Você usou o código para desativar o reator.",
                contexto_atual="O reator desliga com segurança, e o Incidente Zero é evitado. No entanto, a Ordem do Tempo ainda está ativa, e você sente um tremor temporal.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Viajar para 2077 e enfrentar a Ordem", "correta": True, "consequencia": "Você segue a missão.", "proxima_cena": 18},
                    {"texto": "Voltar para 2147", "correta": True, "consequencia": "Você retorna ao futuro.", "proxima_cena": 27},
                    {"texto": "Ficar e investigar mais", "correta": False, "consequencia": "Você é pego.", "proxima_cena": 9}
                ]
            ),
            # Cena 23: Interrogando Clara Mais
            Cena(
                impacto_anterior="Você interrogou Clara mais.",
                contexto_atual="Clara revela que a Ordem planeja usar o reator para viajar a 2077 e consolidar seu poder. Ela te dá coordenadas para o esconderijo deles.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Ir ao esconderijo", "correta": True, "consequencia": "Você enfrenta a Ordem.", "proxima_cena": 17},
                    {"texto": "Desativar o reator", "correta": True, "consequencia": "Você impede o incidente.", "proxima_cena": 22},
                    {"texto": "Deixar Clara e voltar", "correta": False, "consequencia": "Você perde a chance.", "proxima_cena": 13}
                ]
            ),
            # Cena 24: Capturando o Agente
            Cena(
                impacto_anterior="Você capturou o agente da Ordem.",
                contexto_atual="O agente confessa que Clara é apenas uma peão e que a Ordem planeja atacar em 2077. Ele te dá as coordenadas do esconderijo.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Viajar para 2077", "correta": True, "consequencia": "Você enfrenta a Ordem.", "proxima_cena": 18},
                    {"texto": "Desativar o reator agora", "correta": True, "consequencia": "Você impede o incidente.", "proxima_cena": 22},
                    {"texto": "Interrogar o agente mais", "correta": False, "consequencia": "Você perde tempo.", "proxima_cena": 13}
                ]
            ),
            # Cena 25: Juntando-se à Resistência
            Cena(
                impacto_anterior="Você se juntou à resistência.",
                contexto_atual="Ana te leva ao QG da resistência, onde você planeja um ataque à fortaleza da Ordem do Tempo. Você descobre que eles têm um Crono-Núcleo, a fonte do poder temporal.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Atacar a fortaleza", "correta": True, "consequencia": "Você enfrenta a Ordem.", "proxima_cena": 28},
                    {"texto": "Sabotar o Crono-Núcleo", "correta": True, "consequencia": "Você tenta destruí-lo.", "proxima_cena": 29},
                    {"texto": "Recuar e planejar mais", "correta": False, "consequencia": "Você hesita.", "proxima_cena": 4}
                ]
            ),
            # Cena 26: Negociando com a Ordem
            Cena(
                impacto_anterior="Você tentou negociar com a Ordem.",
                contexto_atual="A Ordem aceita sua rendição, mas te engana e desativa seu Crono-Dispositivo. Você é preso em uma cela temporal.",
                chamada_acao="Fim da missão.",
                opcoes=[]
            ),
            # Cena 27: Retorno a 2147 (Final Mediano)
            Cena(
                impacto_anterior="Você voltou para 2147.",
                contexto_atual="O futuro foi parcialmente salvo, mas a Ordem do Tempo ainda existe, e você é rebaixado por não completar a missão. Você vive com arrependimentos.",
                chamada_acao="Fim da missão.",
                opcoes=[]
            ),
            # Cena 28: Ataque à Fortaleza
            Cena(
                impacto_anterior="Você atacou a fortaleza da Ordem.",
                contexto_atual="A resistência invade, mas a Ordem ativa o Crono-Núcleo, criando distorções temporais. Você enfrenta o líder da Ordem, que tenta te apagar do tempo.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Desativar o Crono-Núcleo", "correta": True, "consequencia": "Você tenta pará-lo.", "proxima_cena": 29},
                    {"texto": "Lutar contra o líder", "correta": True, "consequencia": "Você enfrenta o inimigo.", "proxima_cena": 30},
                    {"texto": "Fugir com a resistência", "correta": False, "consequencia": "Você falha.", "proxima_cena": 4}
                ]
            ),
            # Cena 29: Sabotando o Crono-Núcleo
            Cena(
                impacto_anterior="Você tentou sabotar o Crono-Núcleo.",
                contexto_atual="Você desativa o Crono-Núcleo, mas isso cria um colapso temporal. Você tem uma chance de consertar o tempo ou salvar a resistência.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Consertar o tempo", "correta": True, "consequencia": "Você restaura a linha temporal.", "proxima_cena": 31},
                    {"texto": "Salvar a resistência", "correta": True, "consequencia": "Você protege Ana.", "proxima_cena": 32},
                    {"texto": "Fugir do colapso", "correta": False, "consequencia": "Você é apagado.", "proxima_cena": 7}
                ]
            ),
            # Cena 30: Lutando contra o Líder
            Cena(
                impacto_anterior="Você enfrentou o líder da Ordem.",
                contexto_atual="Você derrota o líder, mas o Crono-Núcleo sobrecarrega. Ana te ajuda a desativá-lo, mas o colapso temporal começa.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Consertar o tempo", "correta": True, "consequencia": "Você restaura a linha temporal.", "proxima_cena": 31},
                    {"texto": "Salvar Ana", "correta": True, "consequencia": "Você a protege.", "proxima_cena": 32},
                    {"texto": "Fugir do colapso", "correta": False, "consequencia": "Você é apagado.", "proxima_cena": 7}
                ]
            ),
            # Cena 31: Restaurando o Tempo (Final Épico)
            Cena(
                impacto_anterior="Você consertou o tempo.",
                contexto_atual="O colapso é revertido, e a Ordem do Tempo é destruída. O futuro é salvo, e você é celebrado como o maior crononauta da história.",
                chamada_acao="Fim da missão.",
                opcoes=[]
            ),
            # Cena 32: Salvando a Resistência (Final Bom)
            Cena(
                impacto_anterior="Você salvou Ana e a resistência.",
                contexto_atual="Você protege a resistência, mas o colapso temporal destrói parte do futuro. Você sobrevive com Ana, mas o trabalho de reconstrução apenas começou.",
                chamada_acao="Fim da missão.",
                opcoes=[]
            )
        ]
        return cenas

    def processar_escolha(self, escolha):
        """Processa a escolha do jogador e atualiza o estado."""
        if self.cena_atual >= len(self.cenas):
            return "Fim da missão", False, None
        
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