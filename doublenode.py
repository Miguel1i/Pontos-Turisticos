from pontointeresse import Ponto
from typing import Optional


class DoubleNode:

    def __init__(self, data: Ponto = None, previous: Optional['Ponto'] = None, next: Optional['Ponto'] = None):
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


class LinkedList:

    def __init__(self):
        self._head: DoubleNode = DoubleNode()

    def add(self, ponto: Ponto):
        if self._head is None:
            self._head = DoubleNode(ponto)
        else:
            cursor = self._head
            while cursor.get_next() is not None:
                cursor = cursor.get_next()
            cursor.set_next(ponto)
            ponto.set_previous(cursor)

    def print_lista(self):

        cursor = self._head

        if cursor is None:
            print('Lista Vazia.')
        else:
            while cursor is not None:
                print(cursor.get_data())
                print()
                cursor = cursor.get_next()
