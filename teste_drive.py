from pontointeresse import Ponto
from doublenode import DoubleNode, LinkedList

ponto = Ponto(1, 'Lagoa', 'Rua do Carvão', 37.99, 23.8, 'natureza')
ponto2 = Ponto(1, 'Lagoa Do Fogo', 'Rua do Car', 37.76, 25.8, 'natureza')


node = DoubleNode(ponto)
node2 = DoubleNode(ponto2)

lista = LinkedList()

lista.add(node)
lista.add(node2)
lista.print_lista()
