class TrataDadosBase:
    def __init__(self):
        pass

    def ConstroiListas(self, performanceDados):
        performanceDados = self.verificaBase(performanceDados)
        self.listPartidas(performanceDados)
        performanceDados = self.porcentagemVitorias(performanceDados)
        return performanceDados

    def listPartidas(self, performanceDados):
        partidas = list(range(performanceDados["comum"]["partida"]))
        performanceDados["comum"]["listaPartidas"] = partidas
        return performanceDados

    def porcentagemVitorias(self, performanceDados):
        vitoriaUm = performanceDados["jogadorUm"]["vitoria"]
        vitoriaDois = performanceDados["jogadorDois"]["vitoria"]
        empate = performanceDados["comum"]["empates"]
        listaPartidas = performanceDados["comum"]["listaPartidas"]
        porcentagensUm = []
        porcentagensDois = []
        porcentagensEmpate = []

        for posicao, _ in enumerate(listaPartidas):
            listP = listaPartidas[posicao]
            if listP == 0:
                listP = 1
            porcentagensUm.append(round(vitoriaUm[posicao] * 100 / listP, 2))
            porcentagensDois.append(round(vitoriaDois[posicao] * 100 / listP, 2))
            porcentagensEmpate.append(round(empate[posicao] * 100 / listP, 2))

        performanceDados["jogadorUm"]["porcentagensVitoria"] = porcentagensUm
        performanceDados["jogadorDois"]["porcentagensVitoria"] = porcentagensDois
        performanceDados["comum"]["porcentagensEmpate"] = porcentagensEmpate
        return performanceDados

    def verificaBase(self, performanceDados):
        from model.ArquivosExternos import ArquivosExternos
        if performanceDados is None:
            base = ArquivosExternos()
            base.salva(self.esqueletoPerformance(), 'PerformanceDados')
            return base.pega('PerformanceDados')
        else:
            return performanceDados

    @staticmethod
    def esqueletoPerformance():
        return {
            "jogadorUm": {"tipo": "", "vitoria": [0], "peca": ""},
            "jogadorDois": {"tipo": "", "vitoria": [0], "peca": ""},
            "comum": {"partida": 1, "empates": [0]}
        }
