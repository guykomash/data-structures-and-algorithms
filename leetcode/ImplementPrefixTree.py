class Node:
    def __init__(self):
        self.children = {}
        self.eow = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        if not word: return
        parent = self.root
        i = 0
        while i < len(word):
            if word[i] in parent.children:
                parent = parent.children[word[i]]
            else:
                # rest of the word is not in the tree.
                child = Node()
                parent.children[word[i]] = child
                parent = child
            i = i + 1
            
        parent.eow = True

    def search(self, word: str) -> bool:
        if not word: return True
        parent = self.root
        i = 0
        while i < len(word):
            if word[i] in parent.children:
                parent = parent.children[word[i]]
                if i == len(word) - 1:
                    if parent.eow:
                        return True
                    else: return False
            else:
                return False
            i = i + 1

    def startsWith(self, prefix: str) -> bool:
        if not prefix: return True
        parent = self.root
        i = 0
        while i < len(prefix):
            if prefix[i] in parent.children:
                parent = parent.children[prefix[i]]
                if i == len(prefix) - 1:
                    return True
            else:
                return False
            i = i + 1
