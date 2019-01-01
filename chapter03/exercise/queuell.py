from structures.unorderedlist import UnorderedList


class Queue:
    def __init__(self):
        self._items = UnorderedList()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def is_empty(self):
        return self._items.is_empty()

    def size(self):
        return self._items.size()
