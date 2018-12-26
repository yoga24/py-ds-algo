class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class UnorderedListImpl:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def remove(self,item):
        found = False
        previous = None
        current = self.head
        while current is not None and not found:
            if current.get_data() == item:
                found = True
                break
            else:
                previous = current
                current = current.get_next()
        if current is not None:
            previous.set_next(current.get_next())
            current.set_next(None)
    
    def search(self, item):
        found = False
        current = self.head
        while current is not None:
            if current.get_data() == item:
                found = True
                break
            else:
                current = current.get_next()
        
        return found

    def is_empty(self):
        return self.head is None
    
    def size(self):
        size = 0
        current = self.head
        while current is not None:
            size = size + 1
            current = current.get_next()

        return size

    def append(self, item):
        self.add(item)

    def index(self, item):
        index = -1
        temp_index = 0
        current = self.head
        while current is not None:
            if current.get_data() == item:
                index = temp_index
                break
            else:
                current = current.get_next()
                temp_index += 1
        
        return index

    # insert(self, pos, item):
    # def pop(self, pos = -1):
    #     index = 0
    #     deleted_node = self.head
    #     if self.head is not None:
    #         if pos == -1:
    #             self.head = self.head.get_next()
    #         else:
    #             previous = None
    #             current = self.head
    #             while pos == index and current is not None:
    #                 if current is not 
        
    #     return deleted_node.get_data()
