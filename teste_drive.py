from pontointeresse import Ponto
from doublenode import LinkedList


ponto2 = Ponto(2, 'Lagoa Do Fogo', 'Rua do Car', 37.76, 25.8, 'natureza', [], 0, [], [])

lista = LinkedList()
head = lista.get_head()
cursor = head

lista.add(ponto2)

while cursor is not None:
    print(cursor.get_data())

lista.pesquisa(2)

lista.altera(2, 'restauraçao', 'escadas')

lista.pesquisa(2)

print(lista.get_last_id())
