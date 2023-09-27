class Trie:
    def __init__(self):
        self.char = ""
        self.children = []
        self.isWord = False
        self.wordCount = 0
        
    def insert(self, word: str) -> None:
        if(len(word) == 0):
            self.isWord = True
            return
        for child in self.children:
            if(child.char == word[0]):
                child.insert(word[1:])
                return
        newChild = Trie()
        newChild.char = word[0]
        self.children.append(newChild)
        newChild.insert(word[1:])
        return 

    def search(self, word: str) -> bool:
        if(len(word) == 0):
            return self.isWord
        for child in self.children:
            if(child.char == word[0]):
                return child.search(word[1:])
        return False

    def startsWith(self, prefix: str) -> bool:
        for char in prefix:
            char_not_found = True
            for child in self.children:
                if(child.char == char):
                    char_not_found = False
                    return child.startsWith(prefix[1:])
            if(char_not_found == True):
                return False
        return True