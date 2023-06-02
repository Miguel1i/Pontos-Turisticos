import networkx
from matplotlib import pyplot as p
from Estruturas.Queue.queueinterface import QueueInterface
from Estruturas.Stack.StackInterface import StackInterface


class Grafo:

    def __init__(self):
        self._vertices: dict[str, list[str]] = {}

    def is_empty(self) -> bool:
        return len(self._vertices) == 0

    def adicionar_vertice(self, label: str) -> None:
        if label not in self._vertices:
            self._vertices[label] = []

    def clear(self) -> None:
        self._vertices = {}

    def adicionar_aresta(self, from_label, to_label) -> None:
        if from_label in self._vertices and to_label in self._vertices:
            if to_label not in self._vertices[from_label]:
                self._vertices[from_label].append(to_label)
                self._vertices[to_label].append(from_label)

    def adjacents(self, label):
        if label in self._vertices:
            return self._vertices[label]

    def __str__(self):
        """

        :return:
        """
        s = ""
        for i in self._vertices:
            s += "\nVertex: " + str(i)
            s += " Edges: "
            for a in sorted(self._vertices[i]):
                s += str(a) + "\t"
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

    def get_edges(self) -> list[tuple[str, str]]:

        edges: set[tuple[str, str]] = set()
        for v in self._vertices:
            for adj in self._vertices[v]:
                if (v, adj) not in edges and (adj, v) not in edges:
                    edges.add((v, adj))

        return sorted(edges)

    def get_size_edges(self):
        return len(self.get_edges())

    def get_size_vertices(self):
        return len(self.get_vertices())

    def draw_graph(self):
        """
        Draws the graph
        :return:
        """
        g = networkx.Graph()     # g é do tipo de Networkx
        nodes = self.get_vertices()
        g.add_nodes_from(nodes)
        edges = self.get_edges()
        g.add_edges_from(edges)
        pos = networkx.shell_layout(g)
        networkx.draw_networkx_nodes(g, pos, node_color='red')
        networkx.draw_networkx_edges(g, pos)
        networkx.draw_networkx_labels(g, pos)
        p.show()

    def travessia_largura(self, vertice_inicial: str) -> list[str]:
        """

        :param vertice_inicial:
        :return:
        """
        fila = QueueInterface()
        result = []
        if vertice_inicial in self._vertices:
            fila.add(vertice_inicial)
            while len(fila) > 0:
                front = fila.pop()
                if front not in result:
                    result.append(front)
                for adj in self.adjacents(front):
                    if adj not in result:
                        fila.add(adj)
        return result

    def calcula_caminho(self, vertice_inicial, vertice_final) -> dict:
        result = {}
        fila = QueueInterface()
        if vertice_inicial in self._vertices and vertice_final in self._vertices:
            result[vertice_inicial] = (0, None)
            fila.add((vertice_inicial, 0, None))
            while len(fila) > 0:
                front = fila.pop()
                if front[0] not in result:
                    result[front[0]] = (front[1], front[2])
                for adj in self.adjacents(front[0]):
                    if adj not in result:
                        fila.add((adj, front[1] + 1, front[0]))

        return result

    def mostra_caminho(self, from_label: str, to_label: str) -> list[str]:
        pilha = StackInterface()
        result = self.calcula_caminho(from_label, to_label)
        pilha.push(to_label)
        curr_label = to_label
        while result[curr_label][1] is not None:
            curr_label = result[curr_label][1]
            pilha.push(curr_label)
        return sorted(pilha)
