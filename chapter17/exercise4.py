def autocorrect(self, word):
    currentNode = self.root
    wordFoundSoFar = ""
    for char in word:
        if currentNode.children.get(char):
            wordFoundSoFar += char
            currentNode = currentNode.children.get(char)
        else:
            return wordFoundSoFar + self.collectAllWords(currentNode)[0]
    return word
