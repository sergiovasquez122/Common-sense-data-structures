'''
3. Write an algorithm that finds the greatest value
within a binary search tree
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_greatest(x: Node):
    iterator = x
    if iterator is None:
        return None
    while iterator.left is not None:
        iterator = iterator.left
    return iterator.data
