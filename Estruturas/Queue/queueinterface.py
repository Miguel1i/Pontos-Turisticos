class QueueInterface:
    """ Interface for all ADT queue types. """

    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        :param source_collection: initial content of self
        """
        self.items = []

    # collection accessor methods

    def is_empty(self):
        """
        Tests if self is empty.
        :return: True if len(self) is 0, otherwise False
        """
        return len(self.items) == 0

    def __len__(self):
        """
        Gets the number of items in self.
        :return: the number of items in self
        """
        return len(self.items)

    def __str__(self):
        """
        Builds the string representation of self.
        :return: String representation of self
        """
        return str(self.items)

    def __iter__(self):
        """
        Supports iteration over a view of self.
        :return: an iteration of self
        """
        return iter(self.items)

    # collection mutator methods

    def clear(self):
        """
        Makes self become empty.
        :return: None
        """
        self.items = []

    # Queue accessor methods

    def peek(self):
        """
        Gets the item at the top of the queue, assuming the queue is not empty.
        :return: the top item
        """
        return self.items[0]

    # Queue mutator methods

    def add(self, item):
        """
        Inserts item at the rear of the queue.
        :param item: the item to insert
        :return: None
        """
        self.items.append(item)

    def pop(self):
        """
        Removes the item at top of the queue, assuming the queue is not empty.
        :return the item removed
        """
        self.items.pop(0)
