from pontointeresse import Ponto
from typing import Optional


class DoubleNode:

    def __init__(self, data: Ponto, previous: Optional['Ponto'] = None, next: Optional['Ponto'] = None):
        self._data = data
        self._previous = previous
        self._next = next

    def get_next(self):
        return self._next

    def get_data(self):
        return self._data

    def set_next(self, data):
        self._next = data

    def set_previous(self, data):
        self._previous = data

    def __str__(self):
        return str(self._data)


class LinkedList:

    def __init__(self):
        self._head = None

    def add(self, ponto: Ponto):
        new_node = DoubleNode(ponto)
        if self._head is None:
            self._head = new_node
        else:
            cursor = self._head
            while cursor.get_next() is not None:
                cursor = cursor.get_next()
            cursor.set_next(new_node)

    def print_lista(self):
        cursor = self._head
        if cursor is None:
            print('Lista Vazia.')
        else:
            while cursor is not None:
                print(cursor.get_data())
                print()
                cursor = cursor.get_next()

    def altera(self, _id, categoria, acess):
        cursor = self._head
        while cursor.get_data().get_id() != _id:
            cursor = cursor.get_next()

        cursor.get_data().set_categoria(categoria)
        cursor.get_data().set_acessibilidade(acess)


    def pesquisa(self, _id):
        cursor = self._head
        while cursor.get_data().get_id() != _id:
            cursor = cursor.get_next()
        return cursor.get_data()

    def get_last_id(self):
        cursor = self._head
        if self._head is None:
            return 0
        else:
            while cursor.get_next() is not None:
                cursor = cursor.get_next()
            return  cursor.get_data().get_id()

    def assinala_avalia(self,_id, avalicao: int):
        ponto = self.pesquisa(_id)
        ponto.set_avaliacao(avalicao)
        ponto.set_visitas()
