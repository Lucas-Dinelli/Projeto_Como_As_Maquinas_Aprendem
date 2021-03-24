import networkx as nx
import matplotlib.pyplot as plt
from grafos.Arvore import hierarchy_pos
#from grafos.ScrollWindow import ScrollableWindow
from controller.ControladorDinamicoEmTempoReal import ControladorDinamicoEmTempoReal

fig = plt.figure(1, figsize=(15, 6.5))
G = nx.Graph()
raiz = 0

#preenchimento = Preenchimento()
preenchimento = ControladorDinamicoEmTempoReal()

duplas = preenchimento.duplasDeNosExperimentadas

labels = preenchimento.labelsParaNosExperimentados

#scores = preenchimento.listaDeScores



def ligarRaiz():
    tamanho = len(duplas)
    i = 0
    while i < tamanho:
        if duplas[i][0] < 10 and duplas[i][0] != raiz:
            duplas.insert(i, [raiz, duplas[i][0]])
            tamanho = len(duplas)
            i = i + 1
        elif duplas[i][0] == raiz:
            i = i + 1
        i = i + 1


#ligarRaiz()

labelsExistentes = {}

scoresExistentes = {}


while True:

    print("...")

    if not plt.fignum_exists(1):
        break

    if preenchimento.atualizarDados():

        plt.clf()

        ligarRaiz()

        for dupla in duplas:
            if(dupla in preenchimento.ultimasDuplasjogadas):
                G.add_edge(dupla[0], dupla[1], color='orange') #8080ff
            else:
                G.add_edge(dupla[0], dupla[1], color='green')

        #G.add_edges_from(duplas)

        cores = nx.get_edge_attributes(G, 'color').values()

        pos = hierarchy_pos(G, raiz)

        nx.draw(G, pos=pos, with_labels=False, node_size=5, edge_color=cores)  # node_size = 230

        nx.draw_networkx_labels(G, pos, labels, font_size=9, font_color="black", font_weight="bold")

        preenchimento.mostrarScores(plt, pos)


    plt.pause(0.005)