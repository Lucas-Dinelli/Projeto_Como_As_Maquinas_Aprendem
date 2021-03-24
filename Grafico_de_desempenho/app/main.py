from controller.DesempenhoCtrl import DesempenhoCtrl


class Main:
    def fluxoPrincipal(self):
        DesempenhoCtrl().mandaDadosPraTela()


if __name__ == '__main__':
    Main().fluxoPrincipal()
