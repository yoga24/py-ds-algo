from structures.unorderedlist import UnorderedList


class Stack:
    def __init__(self):
        self._items = UnorderedList()

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def size(self):
        return self._items.size()

    def is_empty(self):
        return self._items.is_empty()