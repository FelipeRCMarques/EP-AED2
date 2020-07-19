from buscaEmLargura import BuscaEmLargura
from Grafo import Grafo
from Grafo import Vertex
from Grafo import Graph
import matplotlib.pyplot as plt
import time
import numpy as np


def executar():

    grafo = Grafo('Enunciado/traducao3.txt')
    arquivo = open('Enunciado/traducao3.txt', 'r')
    lista = arquivo.readlines()
    arquivo.close()

    numero_arestas = int(lista[1])
    numero_vertices = int(lista[0])

    gr = Graph()
    i = 2
    while i <= numero_arestas+1:
        linha = lista[i].split(" ", 2)
        linha[1] = linha[1].replace('\n', '')
        v1 = int(linha[0])
        v2 = int(linha[1])
        gr.add_edge(int(v1), int(v2))
        i += 1

    i = 2
    while i <= numero_arestas+1:
        linha = lista[i].split(" ", 2)
        linha[1] = linha[1].replace('\n', '')
        v1 = int(linha[1])
        v2 = int(linha[0])
        gr.add_edge(int(v1), int(v2))
        i += 1

    vert = gr.get_vertex(364) # conexoes do vertice
    #print(vert)
    #print(len(vert.connected_to)) # grau
    
    i = 0
    distancias = {}
    for i in range(grafo.getV()):
        bfs = BuscaEmLargura(grafo, i)

        for j in range(grafo.getV()):
            if i != j: 
                pilha = bfs.pathTo(j)

                if pilha != []:
                    distancia = pilha.size() - 1

                    # print(f'Entre {i} e {j} = {distancia}')
                    if distancia in distancias.keys():
                        distancias[distancia] += 1
                    else:
                        distancias[distancia] = 1
    
    orderedDict, soma, pesos = {}, 0, 0
    keys = sorted(distancias)
    
    for key in keys:
        orderedDict[key] = int(distancias[key] / 2)
        soma += key * orderedDict[key]
        pesos += orderedDict[key]

    media = soma / pesos
    media_print = str(round(media, 2))
    print(f'Media do diametro: {media_print}')
    
    Yeixo = orderedDict.values()
    Xeixo = orderedDict.keys()

    plt.figure(figsize=(12, 10))
    plt.bar(x=[i for i in range(1, len(Xeixo) + 1)], height=Yeixo, color="grey")
    plt.xticks([i for i in range(1, len(Xeixo) + 1)], labels=Xeixo, rotation='vertical')
    plt.title("Histograma da quantidade de distancias entre pares de nos")
    plt.xlabel("Distancia entre pares de nos")
    plt.ylabel("Quantidade de pares de nos")

    # plt.show()
    plt.savefig("./histograma.png")
    plt.bar(x=[i for i in range(1, len(Xeixo) + 1)], height=Yeixo, log=True, color="red")
    plt.savefig("./histograma_log.png")

if __name__ == "__main__":
    print("Execucao iniciada, por favor aguarde...")

    # define o tempo para comecar a executar
    tempo_para_inicio = time.time()

    # le os dados e executa o metodo de tratamento desses
    executar()

    # imprime o tempo de processamento, que e o tempo executado menos o tempo que levou para iniciar o programa
    print("Tempo de processamento: %s segundos" % (time.time() - tempo_para_inicio))