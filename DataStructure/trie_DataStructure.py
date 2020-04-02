class TrieNode:
    def __init__(self):
        self.childrens = [None]*(26)
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = self.getTrieNode()

    def getTrieNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, string):
        root = self.root
        lenght = len(string)

        for level in range(lenght):
            index = self._charToIndex(string[level])
            if root.childrens[index] == None:
                root.childrens[index] = self.getTrieNode()

            root = root.childrens[index]

        root.isEnd = True

    def search(self, string):
        root = self.root
        length = len(string)

        for level in range(length):
            index = self._charToIndex(string[level])
            if root.childrens[index] == None:
                return False

            root = root.childrens[index]

        return root!=None and root.isEnd

if __name__=="__main__":
    T  = int(input())

    for _ in range(T):
        m = int(input())
        lis = list(map(str, input().split()))
        trie = Trie()
        for ele in lis:
            trie.insert(ele)

        s = str(input())
        print(1 if trie.search(s) else 0)
