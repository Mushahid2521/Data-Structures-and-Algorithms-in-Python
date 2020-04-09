class DisjointSet:
    def __init__(self, matrix):
        self.matrix = matrix
        self.nodesCount = len(matrix)
        self.parent = [i for i in range(self.nodesCount)]

    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


    def union(self, x, y):
        u = self.find(x)
        v = self.find(y)

        if u==v:
            return
        self.parent[u] = v

    def addFriendList(self):
        for i in range(self.nodesCount):
            for j in range(self.nodesCount):
                if self.matrix[i][j] == 1:
                    self.union(i, j)

    def findCircles(self):
        self.addFriendList()
        cnt = 0
        for i in range(self.nodesCount):
            if self.parent[i] == i:
                cnt+=1

        return cnt


mat = [[1,1,0],
 [1,1,1],
 [0,1,1]]
uf = DisjointSet(mat)
print(uf.findCircles())
