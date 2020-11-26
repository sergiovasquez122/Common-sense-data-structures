'''
5. Here's a brillian little linked list puzzle for you. Let's say you have
access to a node from somewhere in the middle of a classic linked list, but not
the linked list itself. That is, you have a variable that points to an instance
of NOde, but you don't have access to the LinkedList instance. In this
situtation, if you follow this node's link,you can find all the items from this
middle node until the end, but you have no way to find the nodes that precede
this node in the list.

write code that will effectively delte this node from the list.
The entire remaining list should remain complete, with only this node removed.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove(x: Node):
    x.data, x.next.data = x.next.data, x.data
    x.next = x.next.next
