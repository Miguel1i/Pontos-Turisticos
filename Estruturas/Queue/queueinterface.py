class Queue:

    def __init__(self, sourceCollection=None):
        self._queue = []
        for item in sourceCollection:
            self._queue.append(item)

    def add(self, item):
        self._queue.append(item)

    def remove(self):
        return self._queue.pop(0)

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)

    def __str__(self):
        return str(self._queue)

    def __iter__(self):
        return iter(self._queue)

    def __len__(self):
        return len(self._queue)
