import matplotlib.pyplot as plt


class TelaDesempenhos:
    def __init__(self):
        self.graficoAtivado = False

    def graficoDesempenho(self, performanceDados):
        tipoUm = performanceDados["jogadorUm"]["tipo"]
        vitoriaUm = performanceDados["jogadorUm"]["vitoria"]
        pecaUm = performanceDados["jogadorUm"]["peca"]
        porcentagensUm = performanceDados["jogadorUm"]["porcentagensVitoria"]

        tipoDois = performanceDados["jogadorDois"]["tipo"]
        vitoriaDois = performanceDados["jogadorDois"]["vitoria"]
        pecaDois = performanceDados["jogadorDois"]["peca"]
        porcentagensDois = performanceDados["jogadorDois"]["porcentagensVitoria"]

        empates = performanceDados["comum"]["empates"]
        listaPartidas = performanceDados["comum"]["listaPartidas"]
        porcentagensEmpate = performanceDados["comum"]["porcentagensEmpate"]

        if not self.graficoAtivado:
            self.graficoAtivado = True
            fig = plt.figure(figsize=(5, 4), facecolor='silver', num='Tela de Desempenhos')
            # fig.canvas.toolbar.pack_forget()  # remove bar inferior

        # plt.cla()  # Clear axis
        plt.clf()  # Clear figure

        plt.plot()
        plt.plot(listaPartidas, porcentagensUm, label=f"{tipoUm} {pecaUm} | {vitoriaUm[-1]}")
        plt.plot(listaPartidas, porcentagensDois, label=f"{tipoDois} {pecaDois} | {vitoriaDois[-1]}")
        plt.plot(listaPartidas, porcentagensEmpate, label=f"Empate | {empates[-1]}")
        plt.xlabel('Partidas')
        plt.ylabel('Vitoria')
        plt.legend()

        plt.tight_layout(w_pad=1.5, h_pad=1.1)

        plt.show(block=False)
        plt.draw()
        plt.pause(0.0001)
