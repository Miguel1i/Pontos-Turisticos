import networkx
from matplotlib import pyplot as p

from Estruturas.Stack.StackInterface import StackInterface
from ViaCirculação.ViaCirculacao import ViaCirculacao


class Grafo:

    def __init__(self):
        self._vertices: dict[str, list[list[str, ViaCirculacao]]] = {}

    def adicionar_vertice(self, label: str) -> None:
        if label not in self._vertices:
            self._vertices[label] = []

    def remover_vertice(self, label: str) -> str | None:
        if label in self._vertices:
            for vertice in self._vertices:
                self.remover_aresta(vertice, label)
            self._vertices.pop(label)
        else:
            return 'Vértice não percente ao grafo!'

    def adicionar_aresta(self, from_label: str, to_label: str, via: ViaCirculacao) -> None:
        if from_label in self._vertices and to_label in self._vertices:
            if to_label not in self._vertices[from_label]:
                self._vertices[from_label].append([to_label, via])

    def remover_aresta(self, from_label, to_label) -> str | None:
        if from_label in self._vertices and to_label in self._vertices:
            for aresta in self._vertices[from_label]:
                if to_label in aresta:
                    self._vertices[from_label].remove(aresta)

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

        fila = [[from_label]]
        caminhos = []

        while fila:
            caminho_atual = fila.pop(0)
            vertice_atual = caminho_atual[-1]

            if vertice_atual == to_label:
                caminhos.append(caminho_atual)

            for lista in self._vertices[vertice_atual]:
                if lista[0] not in caminho_atual:
                    fila.append(caminho_atual + [lista[0]])

        return caminhos

    def calcula_caminho(self, from_label, to_label) -> dict:

        caminhos_possiveis = self.caminhos_possiveis(from_label, to_label)
        resultado = {}

        for caminho in caminhos_possiveis:

            distancia = 0
            tempo_carro = 0
            for i in range(len(caminho) - 1):
                distancia += self.get_distancia_vertices(caminho[i], caminho[i + 1])
                tempo_carro += self.get_velocidade_media(caminho[i], caminho[i + 1])

            resultado[distancia] = [caminho, tempo_carro]

        menor_custo = min(resultado)

        return {
            "Caminho": resultado[menor_custo][0],
            "Distância": menor_custo,
            "Tempo estimado a pé": round(menor_custo / 5, 2),
            "Tempo estimado de carro": round(menor_custo / (resultado[menor_custo][1] / len(resultado[menor_custo][0])),
                                             2)
        }

    def is_empty(self) -> bool:
        return len(self._vertices) == 0

    def clear(self) -> None:
        self._vertices = {}
