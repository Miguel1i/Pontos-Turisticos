class Node:
    """ Represents a linked node"""

    def __init__(self, data, next=None):
        """
        Sets the initial state of self.
        :param data: the value of the node
        :param next: the next node
        """
        self._data = data
        self._next = next

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, valor):

        self._data = valor

    def set_next(self, valor):

        self._next = valor

    def __str__(self) -> str:
        return str(self._data)
