class TrieNode:
    def __init__(self):
        self.childs = [None]*(26)
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
        length = len(string)

        for level in range(length):
            idx = self._charToIndex(string[level])
            if root.childs[idx] == None:
                root.childs[idx] = self.getTrieNode()

            root = root.childs[idx]

        root.isEnd = True

    def search(self, string):
        root = self.root
        length = len(string)
        cnt = 0

        for level in range(length):
            idx = self._charToIndex(string[level])
            if root.childs[idx] == None:
                return cnt

            if root.isEnd == True:
                cnt+=1
            root = root.childs[idx]


        if root!=None and root.isEnd==True:
            cnt+=1

        return cnt

    def solve(self, strings):
        for string in strings:
            self.insert(string)

        res = []
        cn = 0
        for string in strings:
            cn = self.search(string)
            print(cn, string)
            if cn>=2:
                res.append(string)

        return res


if __name__=="__main__":
    trie = Trie()
    strs = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    res = trie.solve(strings=strs)
    print(res)