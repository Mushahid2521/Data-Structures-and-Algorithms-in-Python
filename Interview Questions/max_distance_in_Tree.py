from collections import defaultdict

class Graph:
    def __init__(self, A):
        self.nodes = len(A)
        self.graph = defaultdict(list)
        self.addEdges(A)

    def addEdges(self, A):
        for u, v in enumerate(A):
            if v!=-1:
                self.graph[u].append(v)
                self.graph[v].append(u)

    def findMaxDis(self):
        def distance(node):
            maxVal = 0
            maxNode = 0
            visited = [False]*(self.nodes)
            q, level = [], [0]*(self.nodes+1)

            q.append(node)
            visited[node] = True

            while q:
                u = q.pop()
                for v in self.graph[u]:
                    if visited[v]==False:
                        visited[v] = True
                        q.append(v)
                        level[v] = level[u]+1
                        if level[v]>maxVal:
                            maxVal = level[v]
                            maxNode = v

            return maxVal, maxNode

        _ , n = distance(0)
        maxDis, _ = distance(n)

        return maxDis


class Solution:
    def solve(self, A):
        g  = Graph(A)
        r = g.findMaxDis()
        return r


g = Graph([-1, 0, 0, 0, 3])
print(g.findMaxDis())