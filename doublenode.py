import json
from pontointeresse import Ponto
from typing import Optional
from constantes import ficheiro_json


class DoubleNode:

    def __init__(self, data: Ponto, previous: Optional["Ponto"] = None, _next: Optional["Ponto"] = None):
        """
        Inicializa uma nova instância da classe DoubleNode.
        """
        self._data: Ponto = data
        self._previous: Optional["Ponto"] = previous
        self._next: Optional["Ponto"] = _next

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
        while cursor is not None:
            if cursor.get_data().get_id() == _id:
                break
            cursor = cursor.get_next()

        if cursor:
            return cursor.get_data()

    def get_last_id(self):
        cursor = self._head
        if self._head is None:
            return 0
        else:
            while cursor.get_next() is not None:
                cursor = cursor.get_next()
            return cursor.get_data().get_id()

    def get_head(self) -> DoubleNode | None:
        return self._head

    def set_head(self, valor: None) -> None:
        self._head = valor
