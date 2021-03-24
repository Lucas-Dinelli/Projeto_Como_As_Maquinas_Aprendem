from model.ArquivosExternos import ArquivosExternos
from model.TrataDadosBase import TrataDadosBase
from view.TelaDesempenhos import TelaDesempenhos


class DesempenhoCtrl:
    def mandaDadosPraTela(self):
        telaGrafico = TelaDesempenhos()
        base = ArquivosExternos()
        trataDadosBase = TrataDadosBase()
        while True:
            performanceDados = base.pega('PerformanceDados')
            performanceDados = trataDadosBase.ConstroiListas(performanceDados)
            telaGrafico.graficoDesempenho(performanceDados)
