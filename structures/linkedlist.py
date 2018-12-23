class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head: Node = None

    def add(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            last = self.head
            while last.get_next() is not None:
                last = last.get_next()
            last.set_next(Node(item))

    def remove(self, item):
        prev = None
        curr = self.head
        while curr is not None:
            if curr.get_data() == item:
                if prev is None:
                    self.head = None
                else:
                    prev.set_next(curr.get_next())
                    curr.set_next(None)
            else:
                prev = curr
                curr = curr.get_next()

    def search(self, item):
        curr = self.head
        found = False
        while curr is not None and not found:
            if curr.get_data() == item:
                found = True
            else:
                curr = curr.get_next()
        return found

    def is_empty(self):
        return self.head is None

    def size(self):
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.get_next()
        return count

    def append(self, item):
        curr = self.head
        while curr is not None:
            curr = curr.get_next()
        curr.set_next(Node(item))

    def index(self, item):
        curr = self.head
        index = -1
        temp_index = 0
        while curr is not None:
            if curr.get_data() == item:
                index = temp_index
                break
            else:
                curr = curr.get_next()
            temp_index += 1
        return index

    def insert(self, pos, item):
        index = 0
        prev = None
        curr = self.head

        while pos != index and curr.get_next() is not None:
            index += 1
            prev = curr
            curr = curr.get_next()

        new_node = Node(item)
        if prev is None:
            self.head = new_node
        else:
            prev.set_next(new_node)
            new_node.set_next(curr)

    # def pop(self, pos = None):
    #     deleted_item = None
    #     curr = self.head
    #     if curr is not None:
    #         if curr.get_next() is None:
    #             self.head = None
    #         else:
    #             prev = None
    #             while curr.get_next() is not None:
    #                 prev = curr
    #                 curr = curr.get_next()
    #             deleted_item = curr.get_data
    #             prev.set_next(None)
    #     return deleted_item

    def pop(self, pos=-1):
        index = 0
        prev = None
        curr = self.head

        if curr is None:
            return None

        while pos != index and curr.get_next() is not None:
            index += 1
            prev = curr
            curr = curr.get_next()

        deleted_item = curr.get_data()
        if prev is None:
            self.head = None
        else:
            prev.set_next(curr.get_next())

        return deleted_item
