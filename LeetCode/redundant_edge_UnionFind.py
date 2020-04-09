class UnionFind:
    def __init__(self, n):
        self.graph = [i for i in range(n+1)]

    def find(self, x):
        if x == self.graph[x]:
            return x
        self.graph[x] = self.find(self.graph[x])
        return self.graph[x]

    def union(self, x, y):
        u = self.find(x)
        v = self.find(y)

        if u==v:
            return
        self.graph[u] = v

def solve(edges):
    l = len(edges)+2
    uf = UnionFind(l)

    for edge in edges:
        x,y = uf.find(edge[0]), uf.find(edge[1])
        if x!=y:
            uf.union(edge[0],edge[1])

        else:
            return edge

print(solve([[1,2], [1,3], [2,3]]))
