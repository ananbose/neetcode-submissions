class WordDictionary:

    def __init__(self):
        self.children = {}
        self.eow = False

    def addWord(self, word: str) -> None:
        curr = self
        for i in word:
            if i not in curr.children:
                curr.children[i] = WordDictionary()
            curr = curr.children[i]
        curr.eow = True

    def search(self, word: str) -> bool:
        def dfs(index,node):
            if index == len(word):
                return node.eow
            ch = word[index]
            if ch != '.':
                if ch not in node.children:
                    return False
                else:
                    return dfs(index+1, node.children[ch])
            else:
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False

        
        return dfs(0,self)
