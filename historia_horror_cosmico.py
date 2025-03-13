# historia_horror_cosmico.py
"""
Define a história de horror cósmico 'O Chamado do Abismo Estelar' para o FlowTale.
História não linear com escolhas que afetam atributos como sanidade e a sobrevivência da tripulação.
"""

from cena import Cena

class HistoriaHorrorCosmico:
    def __init__(self):
        self.nome = "O Chamado do Abismo Estelar"
        self.linear = False
        self.cenas = self.inicializar_cenas()
        self.cena_atual = 0
        self.pontuacao = 0
        # Define os atributos extras (neste caso, apenas sanidade)
        self.atributos_extras = {"sanidade": 100}  # Pode ter mais atributos no futuro

    def inicializar_cenas(self):
        """Inicializa as cenas da aventura de horror cósmico."""
        cenas = [
            # Cena 0: Introdução
            Cena(
                impacto_anterior="Você é o capitão de uma expedição espacial em 2199.",
                contexto_atual="Sua nave, a *Aurora Estelar*, chega a um planeta inexplorado chamado Xytheris-9, detectado por sinais anômalos. A tripulação (você, a engenheira Lara, o cientista Dr. Kael e o piloto Theo) desce para explorar. Você encontra ruínas cobertas por símbolos alienígenas pulsantes. Um sussurro ecoa na sua mente: 'Você não deveria estar aqui.'",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Ordenar que Dr. Kael decifre os símbolos", "correta": True, "consequencia": "Você descobre uma mensagem.", "proxima_cena": 1},
                    {"texto": "Explorar as ruínas sozinho", "correta": False, "consequencia": "Você sente algo te observando.", "proxima_cena": 2},
                    {"texto": "Mandar Theo investigar o perímetro", "correta": True, "consequencia": "Theo encontra algo estranho.", "proxima_cena": 3},
                    {"texto": "Voltar para a nave", "correta": False, "consequencia": "Você hesita.", "proxima_cena": 4}
                ]
            ),
            # Cena 1: Decifrando os Símbolos
            Cena(
                impacto_anterior="Você ordenou que Dr. Kael decifrasse os símbolos.",
                contexto_atual="Dr. Kael traduz os símbolos: 'Aqui dorme Zylthara, o Devorador de Estrelas. Não perturbe o selo.' Ele começa a tremer, e você sente um frio na espinha. Sua sanidade diminui (-10).",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Prosseguir e procurar o selo", "correta": True, "consequencia": "Você entra mais fundo nas ruínas.", "proxima_cena": 5},
                    {"texto": "Questionar Dr. Kael sobre Zylthara", "correta": True, "consequencia": "Ele entra em pânico.", "proxima_cena": 6},
                    {"texto": "Abandonar as ruínas e voltar", "correta": False, "consequencia": "Você hesita.", "proxima_cena": 4}
                ]
            ),
            # Cena 2: Explorando Sozinho
            Cena(
                impacto_anterior="Você explorou as ruínas sozinho.",
                contexto_atual="Você encontra um altar com uma esfera negra pulsando. Sussurros invadem sua mente, e você sente sua sanidade escorregar (-20). Você ouve passos atrás de você.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Tocar a esfera", "correta": False, "consequencia": "Você é dominado.", "proxima_cena": 7},
                    {"texto": "Virar-se para enfrentar o que está atrás", "correta": True, "consequencia": "Você encontra algo.", "proxima_cena": 8},
                    {"texto": "Fugir de volta para a tripulação", "correta": True, "consequencia": "Você escapa por pouco.", "proxima_cena": 9}
                ]
            ),
            # Cena 3: Theo Investigando
            Cena(
                impacto_anterior="Você mandou Theo investigar o perímetro.",
                contexto_atual="Theo retorna pálido, dizendo que viu sombras se movendo entre as rochas. Ele ouviu um som como um canto distante, e sua sanidade diminui (-10).",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Ir com Theo investigar as sombras", "correta": True, "consequencia": "Você encontra algo.", "proxima_cena": 10},
                    {"texto": "Ordenar que Dr. Kael decifre os símbolos", "correta": True, "consequencia": "Você busca mais informações.", "proxima_cena": 1},
                    {"texto": "Voltar para a nave", "correta": False, "consequencia": "Você hesita.", "proxima_cena": 4}
                ]
            ),
            # Cena 4: Voltando para a Nave (Final Precoce)
            Cena(
                impacto_anterior="Você decidiu voltar para a nave.",
                contexto_atual="Ao retornar, a nave é engolida por uma fenda dimensional que se abre no planeta. Você e a tripulação são apagados da existência.",
                chamada_acao="Fim da expedição.",
                opcoes=[]
            ),
            # Cena 5: Procurando o Selo
            Cena(
                impacto_anterior="Você prosseguiu para encontrar o selo.",
                contexto_atual="Você entra em uma câmara subterrânea. No centro, há um selo de pedra com tentáculos esculpidos. Lara diz que há energia estranha emanando dele. Você ouve um rugido baixo.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Tentar quebrar o selo", "correta": False, "consequencia": "Você liberta algo terrível.", "proxima_cena": 11},
                    {"texto": "Analisar o selo com Lara", "correta": True, "consequencia": "Você descobre mais.", "proxima_cena": 12},
                    {"texto": "Recuar e planejar", "correta": True, "consequencia": "Você hesita.", "proxima_cena": 9}
                ]
            ),
            # Cena 6: Dr. Kael em Pânico
            Cena(
                impacto_anterior="Você questionou Dr. Kael sobre Zylthara.",
                contexto_atual="Dr. Kael entra em colapso, murmurando que Zylthara é uma entidade que consome mentes. Ele começa a rir histericamente, e sua sanidade cai drasticamente (-20).",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Tentar acalmar Dr. Kael", "correta": True, "consequencia": "Você o estabiliza temporariamente.", "proxima_cena": 13},
                    {"texto": "Prosseguir sem ele", "correta": True, "consequencia": "Você deixa Dr. Kael para trás.", "proxima_cena": 5},
                    {"texto": "Voltar para a nave", "correta": False, "consequencia": "Você desiste.", "proxima_cena": 4}
                ]
            ),
            # Cena 7: Tocando a Esfera (Final Ruim)
            Cena(
                impacto_anterior="Você tocou a esfera negra.",
                contexto_atual="A esfera te engole em uma escuridão infinita. Zylthara desperta dentro da sua mente, e você se torna seu arauto, destruindo a tripulação. Sua sanidade chega a 0.",
                chamada_acao="Fim da expedição.",
                opcoes=[]
            ),
            # Cena 8: Enfrentando o Perigo
            Cena(
                impacto_anterior="Você se virou para enfrentar o que está atrás.",
                contexto_atual="Você vê uma sombra com tentáculos que sussurra seu nome. Sua sanidade diminui (-20), mas você resiste e a sombra recua. Você ouve Lara gritando ao longe.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Correr para ajudar Lara", "correta": True, "consequencia": "Você a encontra.", "proxima_cena": 14},
                    {"texto": "Fugir das ruínas", "correta": True, "consequencia": "Você escapa por pouco.", "proxima_cena": 9},
                    {"texto": "Tentar atacar a sombra", "correta": False, "consequencia": "Você é dominado.", "proxima_cena": 7}
                ]
            ),
            # Cena 9: Recuando
            Cena(
                impacto_anterior="Você recuou ou fugiu das ruínas.",
                contexto_atual="Você retorna ao ponto inicial das ruínas, mas sente que algo te seguiu. A tripulação está nervosa, e Theo sugere voltar à nave.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Voltar para a nave", "correta": False, "consequencia": "Você desiste.", "proxima_cena": 4},
                    {"texto": "Prosseguir com cuidado", "correta": True, "consequencia": "Você entra nas ruínas.", "proxima_cena": 5},
                    {"texto": "Mandar Theo investigar novamente", "correta": True, "consequencia": "Theo encontra algo.", "proxima_cena": 10}
                ]
            ),
            # Cena 10: Investigando as Sombras
            Cena(
                impacto_anterior="Você foi com Theo investigar as sombras.",
                contexto_atual="Entre as rochas, você encontra um cristal que emite luz verde. Ao tocá-lo, visões de Zylthara invadem sua mente, e sua sanidade diminui (-15).",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Guardar o cristal para estudo", "correta": True, "consequencia": "Você leva a prova.", "proxima_cena": 15},
                    {"texto": "Destruir o cristal", "correta": True, "consequencia": "Você o elimina.", "proxima_cena": 16},
                    {"texto": "Deixar o cristal e recuar", "correta": False, "consequencia": "Você hesita.", "proxima_cena": 9}
                ]
            ),
            # Cena 11: Quebrando o Selo (Final Ruim)
            Cena(
                impacto_anterior="Você tentou quebrar o selo.",
                contexto_atual="O selo se parte, e Zylthara desperta. Tentáculos emergem do chão, devorando a tripulação. Você é o último a cair, sua sanidade zerada.",
                chamada_acao="Fim da expedição.",
                opcoes=[]
            ),
            # Cena 12: Analisando o Selo
            Cena(
                impacto_anterior="Você analisou o selo com Lara.",
                contexto_atual="Lara descobre que o selo está ligado a um mecanismo que pode selar Zylthara para sempre, mas requer um sacrifício de energia vital. Sua sanidade diminui (-10).",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Oferecer-se como sacrifício", "correta": True, "consequencia": "Você se arrisca.", "proxima_cena": 17},
                    {"texto": "Pedir que Lara se sacrifique", "correta": False, "consequencia": "Ela se recusa.", "proxima_cena": 18},
                    {"texto": "Procurar outra solução", "correta": True, "consequencia": "Você busca alternativas.", "proxima_cena": 19}
                ]
            ),
            # Cena 13: Acalmando Dr. Kael
            Cena(
                impacto_anterior="Você tentou acalmar Dr. Kael.",
                contexto_atual="Dr. Kael se acalma, mas está abalado. Ele te dá um amuleto que diz ter encontrado nas ruínas, afirmando que pode proteger sua sanidade.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Aceitar o amuleto", "correta": True, "consequencia": "Você ganha proteção.", "proxima_cena": 20},
                    {"texto": "Prosseguir sem Dr. Kael", "correta": True, "consequencia": "Você o deixa para trás.", "proxima_cena": 5},
                    {"texto": "Voltar para a nave", "correta": False, "consequencia": "Você desiste.", "proxima_cena": 4}
                ]
            ),
            # Cena 14: Ajudando Lara
            Cena(
                impacto_anterior="Você correu para ajudar Lara.",
                contexto_atual="Lara está encurralada por uma sombra com tentáculos. Você a salva, mas ela está ferida. Sua sanidade diminui (-15) ao ver a criatura.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Levar Lara de volta à nave", "correta": True, "consequencia": "Você a protege.", "proxima_cena": 21},
                    {"texto": "Continuar explorando com Lara ferida", "correta": True, "consequencia": "Você prossegue.", "proxima_cena": 5},
                    {"texto": "Abandonar Lara", "correta": False, "consequencia": "Você a deixa para trás.", "proxima_cena": 22}
                ]
            ),
            # Cena 15: Guardando o Cristal
            Cena(
                impacto_anterior="Você guardou o cristal para estudo.",
                contexto_atual="O cristal continua a sussurrar em sua mente, mas Dr. Kael diz que pode usá-lo para selar Zylthara. Sua sanidade diminui (-10).",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Prosseguir para o selo", "correta": True, "consequencia": "Você vai mais fundo.", "proxima_cena": 5},
                    {"texto": "Pedir que Dr. Kael analise mais", "correta": True, "consequencia": "Ele estuda o cristal.", "proxima_cena": 23},
                    {"texto": "Destruir o cristal agora", "correta": True, "consequencia": "Você o elimina.", "proxima_cena": 16}
                ]
            ),
            # Cena 16: Destruindo o Cristal
            Cena(
                impacto_anterior="Você destruiu o cristal.",
                contexto_atual="O cristal explode em luz verde, e você ouve um grito sobrenatural. Zylthara está mais próximo de despertar, e sua sanidade diminui (-20).",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Prosseguir para o selo", "correta": True, "consequencia": "Você entra mais fundo.", "proxima_cena": 5},
                    {"texto": "Recuar e planejar", "correta": True, "consequencia": "Você hesita.", "proxima_cena": 9},
                    {"texto": "Voltar para a nave", "correta": False, "consequencia": "Você desiste.", "proxima_cena": 4}
                ]
            ),
            # Cena 17: Sacrifício Pessoal (Final Sacrificial)
            Cena(
                impacto_anterior="Você se ofereceu como sacrifício.",
                contexto_atual="Você usa sua energia vital para ativar o mecanismo. Zylthara é selado, mas você morre no processo. A tripulação sobrevive, mas lamenta sua perda.",
                chamada_acao="Fim da expedição.",
                opcoes=[]
            ),
            # Cena 18: Lara se Recusa
            Cena(
                impacto_anterior="Você pediu que Lara se sacrificasse.",
                contexto_atual="Lara se recusa e foge, tomada pelo medo. Você fica sozinho na câmara, e Zylthara começa a despertar. Sua sanidade diminui (-20).",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Tentar selar Zylthara sozinho", "correta": False, "consequencia": "Você falha.", "proxima_cena": 11},
                    {"texto": "Procurar outra solução", "correta": True, "consequencia": "Você busca alternativas.", "proxima_cena": 19},
                    {"texto": "Fugir da câmara", "correta": True, "consequencia": "Você escapa por pouco.", "proxima_cena": 9}
                ]
            ),
            # Cena 19: Procurando Outra Solução
            Cena(
                impacto_anterior="Você procurou outra solução.",
                contexto_atual="Você encontra uma inscrição que diz que o cristal verde pode selar Zylthara sem sacrifício, mas requer um ritual. Sua sanidade diminui (-10).",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Realizar o ritual com o cristal", "correta": True, "consequencia": "Você tenta o ritual.", "proxima_cena": 24},
                    {"texto": "Voltar para buscar o cristal", "correta": True, "consequencia": "Você retorna.", "proxima_cena": 15},
                    {"texto": "Ignorar e tentar quebrar o selo", "correta": False, "consequencia": "Você falha.", "proxima_cena": 11}
                ]
            ),
            # Cena 20: Aceitando o Amuleto
            Cena(
                impacto_anterior="Você aceitou o amuleto de Dr. Kael.",
                contexto_atual="O amuleto brilha suavemente, e você sente sua sanidade se estabilizar (+10). Dr. Kael te pede para prosseguir com cuidado.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Prosseguir para o selo", "correta": True, "consequencia": "Você entra mais fundo.", "proxima_cena": 5},
                    {"texto": "Mandar Theo investigar novamente", "correta": True, "consequencia": "Theo encontra algo.", "proxima_cena": 10},
                    {"texto": "Voltar para a nave", "correta": False, "consequencia": "Você desiste.", "proxima_cena": 4}
                ]
            ),
            # Cena 21: Levando Lara para a Nave
            Cena(
                impacto_anterior="Você levou Lara de volta à nave.",
                contexto_atual="Lara está segura, mas Theo e Dr. Kael estão desaparecidos. Você ouve um rugido vindo das ruínas. Sua sanidade diminui (-10).",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Voltar para procurar os outros", "correta": True, "consequencia": "Você retorna.", "proxima_cena": 9},
                    {"texto": "Ficar com Lara na nave", "correta": False, "consequencia": "Você desiste.", "proxima_cena": 4},
                    {"texto": "Tentar contatar ajuda externa", "correta": True, "consequencia": "Você busca reforços.", "proxima_cena": 25}
                ]
            ),
            # Cena 22: Abandonando Lara (Final Ruim)
            Cena(
                impacto_anterior="Você abandonou Lara.",
                contexto_atual="Você ouve os gritos de Lara enquanto ela é consumida pela sombra. Sua sanidade colapsa (-50), e você é tomado pela culpa.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Continuar explorando", "correta": True, "consequencia": "Você prossegue.", "proxima_cena": 5},
                    {"texto": "Voltar para a nave", "correta": False, "consequencia": "Você desiste.", "proxima_cena": 4},
                    {"texto": "Tentar se render a Zylthara", "correta": False, "consequencia": "Você é dominado.", "proxima_cena": 7}
                ]
            ),
            # Cena 23: Dr. Kael Analisando o Cristal
            Cena(
                impacto_anterior="Dr. Kael analisou o cristal.",
                contexto_atual="Dr. Kael descobre que o cristal pode selar Zylthara, mas o ritual exige que alguém segure o cristal durante o processo, arriscando a sanidade.",
                chamada_acao="Quem segura o cristal?",
                opcoes=[
                    {"texto": "Você mesmo", "correta": True, "consequencia": "Você se arrisca.", "proxima_cena": 24},
                    {"texto": "Dr. Kael", "correta": True, "consequencia": "Dr. Kael se oferece.", "proxima_cena": 26},
                    {"texto": "Theo", "correta": False, "consequencia": "Theo não resiste.", "proxima_cena": 27}
                ]
            ),
            # Cena 24: Realizando o Ritual (Você)
            Cena(
                impacto_anterior="Você realizou o ritual com o cristal.",
                contexto_atual="Você segura o cristal, e visões de Zylthara te atacam. Sua sanidade diminui (-30), mas o selo começa a brilhar. Você está quase lá.",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Continuar o ritual", "correta": True, "consequencia": "Você termina o processo.", "proxima_cena": 28},
                    {"texto": "Parar para se salvar", "correta": False, "consequencia": "Você falha.", "proxima_cena": 11},
                    {"texto": "Pedir ajuda a alguém", "correta": True, "consequencia": "Alguém te ajuda.", "proxima_cena": 29}
                ]
            ),
            # Cena 25: Contatando Ajuda Externa
            Cena(
                impacto_anterior="Você tentou contatar ajuda externa.",
                contexto_atual="Você envia um sinal de socorro, mas a resposta é um silêncio assustador. Uma fenda dimensional se abre, e a nave é destruída.",
                chamada_acao="Fim da expedição.",
                opcoes=[]
            ),
            # Cena 26: Dr. Kael no Ritual
            Cena(
                impacto_anterior="Dr. Kael segurou o cristal durante o ritual.",
                contexto_atual="Dr. Kael resiste por um tempo, mas Zylthara o domina. Ele se torna um servo da entidade, e o selo se quebra. Sua sanidade diminui (-20).",
                chamada_acao="O que você faz?",
                opcoes=[
                    {"texto": "Lutar contra Dr. Kael", "correta": True, "consequencia": "Você tenta detê-lo.", "proxima_cena": 30},
                    {"texto": "Fugir da câmara", "correta": True, "consequencia": "Você escapa.", "proxima_cena": 9},
                    {"texto": "Tentar selar Zylthara sozinho", "correta": False, "consequencia": "Você falha.", "proxima_cena": 11}
                ]
            ),
            # Cena 27: Theo no Ritual (Final Ruim)
            Cena(
                impacto_anterior="Theo segurou o cristal.",
                contexto_atual="Theo não resiste à influência de Zylthara e é consumido. O selo se quebra, e Zylthara desperta, destruindo tudo.",
                chamada_acao="Fim da expedição.",
                opcoes=[]
            ),
            # Cena 28: Concluindo o Ritual (Final Bom)
            Cena(
                impacto_anterior="Você continuou o ritual.",
                contexto_atual="O cristal brilha intensamente, e Zylthara é selado. Você sobrevive, mas sua sanidade está quase zerada. A tripulação te agradece, mas você nunca será o mesmo.",
                chamada_acao="Fim da expedição.",
                opcoes=[]
            ),
            # Cena 29: Pedindo Ajuda no Ritual
            Cena(
                impacto_anterior="Você pediu ajuda durante o ritual.",
                contexto_atual="Lara se junta a você, e juntos vocês completam o ritual. Zylthara é selado, e ambos sobrevivem, mas sua sanidade está abalada (-20).",
                chamada_acao="Fim da expedição.",
                opcoes=[]
            ),
            # Cena 30: Lutando contra Dr. Kael
            Cena(
                impacto_anterior="Você lutou contra Dr. Kael.",
                contexto_atual="Você derrota Dr. Kael, mas ele te amaldiçoa com visões de Zylthara. Sua sanidade colapsa (-50), e você desmaia enquanto o selo se quebra.",
                chamada_acao="O que acontece?",
                opcoes=[
                    {"texto": "Tentar selar Zylthara", "correta": False, "consequencia": "Você falha.", "proxima_cena": 11},
                    {"texto": "Fugir com os outros", "correta": True, "consequencia": "Você escapa.", "proxima_cena": 31},
                    {"texto": "Aceitar o destino", "correta": False, "consequencia": "Você é dominado.", "proxima_cena": 7}
                ]
            ),
            # Cena 31: Fugindo com os Outros (Final Mediano)
            Cena(
                impacto_anterior="Você fugiu com os outros.",
                contexto_atual="Você e os sobreviventes voltam à nave e escapam de Xytheris-9, mas Zylthara desperta e começa a consumir o sistema estelar. Você sobrevive, mas à custa de muitos.",
                chamada_acao="Fim da expedição.",
                opcoes=[]
            )
        ]
        return cenas

    def processar_escolha(self, escolha):
        """Processa a escolha do jogador e atualiza o estado."""
        if self.cena_atual >= len(self.cenas):
            return "Fim da expedição", False, None
        
        consequencia, correta, proxima_cena = self.cenas[self.cena_atual].processar_escolha(escolha)
        print(f"Processando escolha: Cena atual {self.cena_atual}, Próxima cena {proxima_cena}, Correta: {correta}")

        # Ajustar atributos extras (neste caso, sanidade) com base nas escolhas
        sanidade_perda = 0
        if self.cena_atual == 1 or self.cena_atual == 3 or self.cena_atual == 12 or self.cena_atual == 15 or self.cena_atual == 16 or self.cena_atual == 19 or self.cena_atual == 21:
            sanidade_perda = 10
        elif self.cena_atual == 2 or self.cena_atual == 6 or self.cena_atual == 8 or self.cena_atual == 14 or self.cena_atual == 18 or self.cena_atual == 26 or self.cena_atual == 29:
            sanidade_perda = 20
        elif self.cena_atual == 10:
            sanidade_perda = 15
        elif self.cena_atual == 22:
            sanidade_perda = 50
        elif self.cena_atual == 24:
            sanidade_perda = 30
        elif self.cena_atual == 20:
            sanidade_perda = -10  # Ganho de sanidade

        self.atributos_extras["sanidade"] -= sanidade_perda
        if self.atributos_extras["sanidade"] <= 0:
            self.cena_atual = 7  # Cena de colapso mental
            self.pontuacao = -99999
            print(f"Sanidade zerada: {self.atributos_extras['sanidade']}, direcionando para cena 7")
            return "Sua sanidade colapsou", False, 7

        if proxima_cena is not None:
            self.cena_atual = proxima_cena
            self.pontuacao += 10 if correta else -5
            print(f"Atualizado: Cena {self.cena_atual}, Pontuação {self.pontuacao}, Atributos Extras {self.atributos_extras}")
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
            "pontuacao": self.pontuacao,
            "atributos_extras": self.atributos_extras  # Salva os atributos extras
        }

    @classmethod
    def from_dict(cls, data):
        """Desserializa a história a partir de um dicionário."""
        historia = cls()
        historia.nome = data["nome"]
        historia.linear = data["linear"]
        historia.cena_atual = data["cena_atual"]
        historia.pontuacao = data["pontuacao"]
        historia.atributos_extras = data.get("atributos_extras", {"sanidade": 100})  # Restaura atributos extras
        historia.cenas = [Cena(**c) for c in data["cenas"]]
        return historia