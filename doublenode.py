import json
from pontointeresse import Ponto
from typing import Optional
import math as m
from constantes import R, ficheiro_json


class DoubleNode:

    def __init__(self, data: Ponto, previous: Optional['Ponto'] = None, _next: Optional['Ponto'] = None):
        """
        Inicializa uma nova instância da classe DoubleNode.
        """
        self._data: Ponto = data
        self._previous: Optional['Ponto'] = previous
        self._next: Optional['Ponto'] = _next

    def get_next(self) -> Ponto | None:
        """
        Obtém o próximo nó da lista encadeada.
        :returns:
        Ponto: Objeto Ponto armazenado no nó.
        None: Se este for o último nó.
        """
        return self._next

    def get_data(self) -> Ponto:
        """
        Método de obtenção do ponto armazenado no nó.
        :return: Ponto: Objeto ponto armazenado no nó.
        """
        return self._data

    def set_next(self, data) -> None:
        """
        Define o próximo nó na lista encadeada.
        :return: None
        """
        self._next = data

    def set_previous(self, data) -> None:
        """
        Define o nó anterior na lista encadeada.
        :return: None
        """
        self._previous = data

    def __str__(self) -> str:
        """
        Método de obtenção da representação do objeto Ponto armazenado no nó.
        :return: Str: ‘String’ que representa o objeto Ponto armazenado no nó
        """
        return str(self._data)


class LinkedList:

    def __init__(self):
        self._head = None
        with open(ficheiro_json, "r") as f:
            data = json.load(f)
            for p in data:
                ponto = Ponto(data[p]["id"], data[p]["designacao"], data[p]["Morada"], data[p]["Latitude"],
                              data[p]["Longitude"], data[p]["categoria"], data[p]["acess"], data[p]["visitas"],
                              data[p]["avaliacao"], data[p]["geo"],
                              data[p]["Suges"])
                self.add(ponto)

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
            if len(cursor.get_data().get_avaliacao()) > 0:
                media = sum(cursor.get_data().get_avaliacao()) / len(cursor.get_data().get_avaliacao())
                print(
                    f'\nID: {ponto.get_id()} \nDesignação: {ponto.get_designacao()} \nMorada: {ponto.get_morada()}'
                    f' \nSugestoes: {str(ponto.get_sugestoes())} '
                    f'\nMédia: {media} \nVisitas: {ponto.get_visitas()}\n')
            else:
                print(
                    f'\nID: {ponto.get_id()} \nDesignação: {ponto.get_designacao()} \nMorada: {ponto.get_morada()}'
                    f' \nSugestoes: {str(ponto.get_sugestoes())} '
                    f'\nMédia: {0} \nVisitas: {ponto.get_visitas()}\n')
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
            a = m.sin(lat_diference / 2) ** 2 + m.cos(lat1) * m.cos(lat2) * m.sin(lon_diference / 2) ** 2
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

    def grava(self):
        cursor = self._head
        with open(ficheiro_json, "r") as f:
            data = json.load(f)
            while cursor is not None:
                data.update({str(cursor.get_data().get_id()): {"id": int(cursor.get_data().get_id()),
                                                               "designacao": str(cursor.get_data().get_designacao()),
                                                               "Morada": str(cursor.get_data().get_morada()),
                                                               "Latitude": float(
                                                                   cursor.get_data().get_coordenadas().get_latitude()),
                                                               "Longitude": float(
                                                                   cursor.get_data().get_coordenadas().get_longitude()),
                                                               "categoria": str(cursor.get_data().get_categoria()),
                                                               "acess": cursor.get_data().get_acessibilidade(),
                                                               "geo": cursor.get_data().get_geo(),
                                                               "Suges": cursor.get_data().get_sugestoes(),
                                                               "avaliacao": cursor.get_data().get_avaliacao(),
                                                               "visitas": cursor.get_data().get_visitas()}})
                cursor = cursor.get_next()

        with open(ficheiro_json, "w") as file:
            json.dump(data, file, indent=2)


def ordena_pesquisa(lista_de_pontos: list) -> list:
    """
    Ordena a lista de objetos Ponto por ordem alfabética da designação.
    :param lista_de_pontos: List: lista de objetos Ponto a ser ordenada.
    :return: List: Lista ordenada por ordem alfabética da designação.
    """
    for i in range(1, len(lista_de_pontos)):
        key = lista_de_pontos[i]

        j = i - 1

        while j >= 0 and key.get_designacao() < lista_de_pontos[j].get_designacao():
            lista_de_pontos[j + 1] = lista_de_pontos[j]
            j = j - 1

        lista_de_pontos[j + 1] = key

    return lista_de_pontos


def ordena_sugestoes(lista_de_pontos: list) -> list:
    """
    Ordena uma lista de objetos Ponto com base no número de visitas.
    :param lista_de_pontos: List: lista de objetos Ponto a ser ordenada.
    :return: List: lista de objetos Ponto ordenada pelo número de visitas.
    """

    if len(lista_de_pontos) > 1:

        pivo = len(lista_de_pontos) // 2
        direita = lista_de_pontos[:pivo]
        esquerda = lista_de_pontos[pivo:]

        ordena_sugestoes(direita)
        ordena_sugestoes(esquerda)

        i = j = k = 0

        while i < len(direita) and j < len(esquerda):
            if direita[i].get_visitas() > esquerda[j].get_visitas():
                lista_de_pontos[k] = direita[i]
                i += 1
            else:
                lista_de_pontos[k] = esquerda[j]
                j += 1
            k += 1

        while i < len(direita):
            lista_de_pontos[k] = direita[i]
            i += 1
            k += 1

        while j < len(esquerda):
            lista_de_pontos[k] = esquerda[j]
            j += 1
            k += 1

    return lista_de_pontos
