import networkx
from matplotlib import pyplot as p
from ViaCirculacao.ViaCirculacao import ViaCirculacao
from Estruturas.Queue.queueinterface import Queue


class Grafo:

    def __init__(self):
        self._vertices: dict[str, list[list[str, ViaCirculacao]]] = {}

    def adicionar_vertice(self, label: str) -> str:
        if label not in self._vertices:
            self._vertices[label] = []
            return 'Vertice Adicionado'
        else:
            return 'O Ponto já se encontra na rede'

    def remover_vertice(self, label: str) -> str | None:
        if label in self._vertices:
            for vertice in self._vertices:
                self.remover_aresta(vertice, label)
            self._vertices.pop(label)
            return 'Vértice removido com sucesso'
        else:
            return 'Vértice não percente à rede!'

    def adicionar_aresta(self, from_label: str, to_label: str, via: ViaCirculacao) -> str:
        if from_label in self._vertices and to_label in self._vertices:
            if to_label not in self._vertices[from_label]:
                self._vertices[from_label].append([to_label, via])
                return 'Aresta adicionada com sucesso'
            else:
                return 'Aresta já existe'

    def remover_aresta(self, from_label, to_label) -> str:
        if (from_label, to_label) in self.get_edges():
            for aresta in self._vertices[from_label]:
                if to_label in aresta:
                    self._vertices[from_label].remove(aresta)
            return 'Aresta removida com Sucesso'
        else:
            return 'Aresta inválida!'

    def adjacents(self, label: str):
        if label in self._vertices:
            adjacentes = []
            for aresta in self._vertices[label]:
                adjacentes.append(aresta[0])

            return adjacentes

    def adjacents_vias(self, label: str):
        if label in self._vertices:
            adjacentes = []
            for aresta in self._vertices[label]:
                adjacentes.append((aresta[0], aresta[1]))

            return adjacentes

    def __str__(self):
        """

        :return:
        """
        s = ''
        for v in self._vertices:
            s += f'{v} -> {self._vertices[v]}\n'
        return s

    def __len__(self):
        """
        :return:
        """
        return len(self._vertices)

    def get_vertices(self) -> set[str]:
        """
        :return:
        """
        return set(self._vertices.keys())

    def get_edges(self) -> set[tuple[str, list[str, ViaCirculacao]]]:

        edges: set[tuple[str, list[str, ViaCirculacao]]] = set()
        for v in self._vertices:
            for adj, i in self._vertices[v]:
                if (v, adj) not in edges and (adj, v) not in edges:
                    edges.add((v, adj))

        return edges

    def get_size_edges(self):
        return len(self.get_edges())

    def get_size_vertices(self):
        return len(self.get_vertices())

    def draw_graph(self):
        """
        Draws the graph
        :return:
        """
        g = networkx.DiGraph()  # g é do tipo de Networkx
        g.add_nodes_from(self.get_vertices())
        g.add_edges_from(self.get_edges())
        networkx.draw(g, with_labels=True, arrows=True)
        p.show()

    def get_distancia_vertices(self, from_label, to_label):
        for aresta in self._vertices[from_label]:
            if to_label == aresta[0]:
                return aresta[1].get_distancia()

    def get_velocidade_media(self, from_label, to_label):
        for aresta in self._vertices[from_label]:
            if to_label == aresta[0]:
                return aresta[1].get_velocidade_media_circulacao()

    def caminhos_possiveis(self, from_label, to_label):
        """
        Retorna todos os caminhos possiveis entre 2 pontos da rede
        :param from_label:
        :param to_label:
        :return caminhos:
        """

        fila = [[from_label]]
        caminhos = []
        if from_label in self._vertices and to_label in self._vertices:
            while fila:
                caminho_atual = fila.pop(0)
                vertice_atual = caminho_atual[-1]

                if vertice_atual == to_label:
                    caminhos.append(caminho_atual)

                for lista in self._vertices[vertice_atual]:
                    if lista[0] not in caminho_atual:
                        fila.append(caminho_atual + [lista[0]])

            return caminhos

    def calcula_caminho(self, from_label, to_label) -> dict | str:

        """
        Retorna o caminho mais curto entre 2 pontos da rede -> CAminho / Distancia(custo) / tempo a pé / tempo de carro
        :param from_label:
        :param to_label:
        :return:
        """

        caminhos_possiveis = self.caminhos_possiveis(from_label, to_label)
        resultado = {}

        for caminho in caminhos_possiveis:

            distancia = 0
            tempo_carro = 0
            for i in range(len(caminho) - 1):
                distancia += self.get_distancia_vertices(caminho[i], caminho[i + 1])
                tempo_carro += self.get_velocidade_media(caminho[i], caminho[i + 1])

            resultado[distancia] = [caminho, tempo_carro]
        if resultado.__len__() > 0:
            menor_custo = min(resultado)
        else:
            return 'Não foi possivel encontrar caminho entre esse pontos'

        return {
            "Caminho": resultado[menor_custo][0],
            "Distância": menor_custo,
            "Tempo estimado a pé": round(menor_custo / 5, 2),
            "Tempo estimado de carro": round(menor_custo / (resultado[menor_custo][1] / len(resultado[menor_custo][0])),
                                             2)
        }

    def ponto_maios_saidas(self) -> str:
        """
        Retorna o/os pontos que contem mais saidas
        :return:
        """
        maior = {}
        for vertice in self._vertices:
            if len(self._vertices[vertice]) not in maior:
                maior[len(self._vertices[vertice])] = [vertice]
            else:
                maior[len(self._vertices[vertice])] += [vertice]
        return f'{maior[max(maior)]}, {max(maior)}'

    def ponto_mais_entradas(self) -> str:
        """
        Retorna o/os pontos que contem mais entradas
        :return:
        """
        maior = {}
        count = 0
        for vertice in self._vertices:
            for aresta in self.get_edges():
                if vertice in aresta[1]:
                    count += 1
            if count not in maior:
                maior[count] = [vertice]
            else:
                maior[count] += [vertice]
            count = 0
        return f'{maior[max(maior)]}, {max(maior)}'





    def arvore(self, from_label: str) -> None:

        travessia = self.travessia_largura(from_label)
        g = networkx.DiGraph()
        g.add_nodes_from(travessia)
        i = 0
        while i < len(travessia):
            adjacentes = self.adjacents(travessia[i])

            arestas = []
            for adjacente in adjacentes:
                arestas.append((travessia[i], adjacente))

            g.add_edges_from(arestas)
            i += 1

        pos = networkx.shell_layout(g)
        # draw Grafo na forma de arvore
        networkx.draw(g, pos=pos, with_labels=True, arrows=True)
        p.show()

    def travessia_largura(self, vertice_inicial: str) -> list:
        """
        Algoritmo de travessia em largura de um grafo.
        :param vertice_inicial: Vértice por onde irá ser iniciada a travessia.
        :return:
            List:
                []: Caso o vértice não pertencer ao grafo.
                [travessia]: Lista de vértices visitados.
        """
        visitados: list = []  # Lista de vértices visitados.

        # Verifica se o vértice pertence ao grafo.
        if vertice_inicial in self._vertices.keys():

            # Fila que contém o primeiro vértice.
            fila: Queue = Queue([vertice_inicial])

            # Enquanto a fila não estiver vazia.
            while fila:
                # Remove o vértice da fila.
                vertice = fila.remove()

                # Se o vértice não estiver na lista de visitados.
                if vertice not in visitados:
                    # É adicionado à lista de visitados.
                    visitados.append(vertice)

                    vizinhos = []  # Lista de vértices ligados ao vértice (vizinhos).
                    for aresta in self._vertices[vertice]:
                        vizinhos.append(aresta[0])

                    for vizinho in vizinhos:
                        # Se o vértice vizinho não estiver contido na lista de vértices visitados.
                        if vizinho not in visitados:
                            # É adicionado à fila.
                            fila.add(vizinho)

        return visitados

    def is_empty(self) -> bool:
        return len(self._vertices) == 0

    def clear(self) -> None:
        self._vertices = {}
