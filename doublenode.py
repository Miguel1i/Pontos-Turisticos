from pontointeresse import Ponto
from typing import Optional
import math as m
from variable import R


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

    def pesquisa(self, _id: int):
        cursor = self._head
        while cursor.get_data().get_id() != _id:
            cursor = cursor.get_next()
        return cursor.get_data()

    def pesquisa_por_categoria(self, _categoria: str):
        cursor = self._head
        pontos = []

        while cursor is not None:
            pontos.append(cursor.get_data())
            cursor = cursor.get_next()

        self._head = None
        for i in ordena_pesquisa(pontos):
            self.add(i)

        cursor = self._head
        flag = 1
        while cursor is not None:
            if cursor.get_data().get_categoria().lower() == _categoria.lower():
                print(cursor.get_data())
                flag += 1
            cursor = cursor.get_next()

        if flag == 1:
            print('Não existe nenhum Ponto de Interesse com esta categoria.')

    def consultar_estatisticas(self):
        cursor = self._head

        while cursor is not None:
            ponto = cursor.get_data()
            media = sum(cursor.get_data().get_avaliacao()) / len(cursor.get_data().get_avaliacao())
            print(
                f'\nID: {ponto.get_id()} \nDesignação: {ponto.get_designacao()} \nMédia: {media} \nVisitas: {ponto.get_visitas()}\n')
            cursor = cursor.get_next()

    def obter_sugestoes(self, latitude: float, longitude: float):
        cursor = self._head
        pontos = []

        while cursor is not None:
            pontos.append(cursor.get_data())
            cursor = cursor.get_next()

        self._head = None
        for i in ordena_sugestoes(pontos):
            self.add(i)

        cursor = self._head
        flag = 1
        while cursor is not None:
            ponto = cursor.get_data().get_coordenadas()
            lat_diference = m.radians(latitude - ponto.get_latitude())
            lon_diference = m.radians(longitude - ponto.get_longitude())
            lat1 = m.radians(latitude)
            lat2 = m.radians(ponto.get_latitude())
            a = m.sin(lat_diference / 2)**2 + m.cos(lat1) * m.cos(lat2) * m.sin(lon_diference / 2)**2
            c = 2 * m.asin(m.sqrt(a))
            d = R * c

            if d <= 50:
                print(cursor.get_data())
                flag += 1

            cursor = cursor.get_next()

        if flag == 1:
            print('Não existe nenhum Ponto de Interesse perto.')

    def get_last_id(self):
        cursor = self._head
        if self._head is None:
            return 0
        else:
            while cursor.get_next() is not None:
                cursor = cursor.get_next()
            return cursor.get_data().get_id()

    def assinala_avalia(self, _id, avalicao: int):
        ponto = self.pesquisa(_id)
        ponto.set_avaliacao(avalicao)
        ponto.set_visitas()


def ordena_pesquisa(lista_de_pontos: list):
    for i in range(1, len(lista_de_pontos)):
        key = lista_de_pontos[i]

        j = i - 1

        while j >= 0 and key.get_designacao() < lista_de_pontos[j].get_designacao():
            lista_de_pontos[j + 1] = lista_de_pontos[j]
            j = j - 1

        lista_de_pontos[j + 1] = key

    return lista_de_pontos


def ordena_sugestoes(lista_de_pontos: list):
    if len(lista_de_pontos) > 1:

        r = len(lista_de_pontos) // 2
        L = lista_de_pontos[:r]
        M = lista_de_pontos[r:]

        ordena_sugestoes(L)
        ordena_sugestoes(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i].get_visitas() > M[j].get_visitas():
                lista_de_pontos[k] = L[i]
                i += 1
            else:
                lista_de_pontos[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            lista_de_pontos[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            lista_de_pontos[k] = M[j]
            j += 1
            k += 1

    return lista_de_pontos
