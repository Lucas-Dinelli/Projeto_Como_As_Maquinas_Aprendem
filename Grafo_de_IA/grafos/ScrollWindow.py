import matplotlib

# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from controller.Preenchimento import Preenchimento as preenchimento


class ScrollableWindow(QtWidgets.QMainWindow):
    def __init__(self, fig, pos, listaDeScores):
        self.pos = pos
        self.listaDeScores = listaDeScores
        # self.formatarListaDePosicoes()

        self.qapp = QtWidgets.QApplication([])

        QtWidgets.QMainWindow.__init__(self)
        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(QtWidgets.QVBoxLayout())
        self.widget.layout().setContentsMargins(0, 0, 0, 0)
        self.widget.layout().setSpacing(0)

        self.fig = fig
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.scroll = QtWidgets.QScrollArea(self.widget)
        self.scroll.setWidget(self.canvas)

        self.nav = NavigationToolbar(self.canvas, self.widget)
        self.widget.layout().addWidget(self.nav)
        self.widget.layout().addWidget(self.scroll)

        plt.xlim([-0.001, 1.008])  # 1.042361111111111

        # self.setMousePosition()

        preenchimento.mostrarScores(self, plt, pos)

        self.show()

        exit(self.qapp.exec_())
