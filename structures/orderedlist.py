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


class OrderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        ll_str = []
        current = self.head
        while current is not None:
            ll_str.append(current.get_data())
            current = current.get_next()
        return str(ll_str)

    def add(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            previous = None
            current = self.head
            while current is not None:
                if current.get_data() > item:
                    break
                else:
                    previous = current
                    current = current.get_next()

            new_node = Node(item)
            if previous is None:
                new_node.set_next(self.head)
                self.head = new_node
            else:
                new_node.set_next(previous.get_next())
                previous.set_next(new_node)

    def remove(self, item):
        if self.head is None:
            return

        current = self.head
        previous = None
        while current is not None:
            if current.get_data() == item:
                break
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
            current.set_next(None)
        else:
            previous.set_next(current.get_next())
            current.get_next(None)

    def search(self, item):
        found = False
        current = self.head
        while current is not None and current.get_data() <= item:
            if current.get_data() == item:
                found = True
                break
            else:
                current = current.get_next()

        return found

    def is_empty(self):
        return self.head is None

    def index(self, item):
        index = -1
        temp_index = 0
        current = self.head
        while current is not None and current.get_data() <= item:
            if current.get_data() == item:
                index = temp_index
                break
            else:
                current = current.get_next()
                temp_index += 1

        return index

    def pop(self, pos=-1):
        deleted_item = None
        index = 0
        if self.head is not None:
            previous = None
            current = self.head
            while pos != index and current.get_next() is not None:
                previous = current
                current = current.get_next()
                index += 1

            deleted_item = current.get_data()

            if previous is not None:
                previous.set_next(current.get_next())
                current.set_next(None)
            else:
                self.head = None

        return deleted_item
