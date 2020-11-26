'''
add a method to the classic LinkedList class that prints all the elements of the list.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def search(self, key):
        iterator = self.head
        while iterator is not None:
            if iterator.data == key:
                return iterator
            iterator = iterator.next
        return None

    def __str__(self):
        iterator = self.head
        s = ""
        while iterator is not None:
            s += str(iterator.data) + " "
            iterator = iterator.next
        return s

    def last_element(self):
        iterator = self.head
        while iterator is not None and iterator.next is not None:
            iterator = iterator.next
        return iterator.data if iterator is not None else None
