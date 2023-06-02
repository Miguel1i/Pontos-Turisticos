from grafo import Grafo


def grafo_1(g: Grafo) -> None:
    print(g)
    #g.draw_graph()
    for i in sorted(g.get_vertices()):
        print(i , ": ", g.travessia_largura(i))

def create_graph() -> Grafo:
    g = Grafo()
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    for vertice in vertices:
        g.adicionar_vertice(vertice)
    arestas = [("A", "B"), ("A", "C"), ("A", "E"), ("B", "C"), ("B", "D"), ("C", "E"), ("C", "D"), ("D", "F"), ("E", "F")]
    for a in arestas:
        g.adicionar_aresta(a[0], a[1])
    return g


grafo_1(create_graph())
