from Trie import *

def traverse(self, node=None):
    currentNode = self or self.root

    for key, childNode in currentNode.children.items():
        print(key)
        if key != "*":
            self.traverse(childNode)
