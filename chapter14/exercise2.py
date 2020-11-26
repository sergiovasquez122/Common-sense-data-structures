'''
2. Add a method to the DoublyLinkedList class that prints all the elements of
the list in reverse order.
'''
class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.next = prev
        self.prev = next

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def reverse_print(self):
        iterator = self.tail
        s = ""
        while iterator is not None:
            s += str(iterator.data) + " "
            iterator = iterator.prev
        return s
