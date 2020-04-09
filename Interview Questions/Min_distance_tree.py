from collections import defaultdict
import collections

class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.graph = defaultdict(list)
        self.addEdges(edges)

    def addEdges(self, edges):
        for edge in edges:
            u,v = edge[0], edge[1]
            self.graph[u].append(v)
            self.graph[v].append(u)

    def findMin(self):
        # Not the fast solution
        def bfs(node):
            visited = [False]*(self.n+1)
            q = []
            level = [0]*(self.n+1)
            maxLevel = 0
            q.append(node)
            visited[node] = True
            while q:
                u = q.pop()
                for v in self.graph[u]:
                    if visited[v]==False:
                        visited[v] = True
                        q.append(v)
                        level[v] = level[u]+1
                        if level[v]>maxLevel:
                            maxLevel = level[v]

            return maxLevel

        node_level = defaultdict(list)
        minL = float("inf")
        for node in range(self.n):
            l = bfs(node)
            if l<minL:
                minL = l
            node_level[l].append(node)

        return node_level[minL]

g = Graph(4, [[1, 0], [1, 2], [1, 3]])
print(g.findMin())


# # Solution from LeetCode. Not Understood

# class Solution(object):
#     def findMinHeightTrees(self, n, edges):
#         if n == 1:
#             return [0]
#         graph = collections.defaultdict(list)
#         queue = collections.deque()
#         indegree = [0]*n
#         #undirected graph in adjacency list， and update the degree for each node,
# 		#remember it's undirected graph
#         for pair in edges:
#             graph[pair[0]].append(pair[1])
#             graph[pair[1]].append(pair[0])
#             indegree[pair[0]] +=1
#             indegree[pair[1]] +=1
#             #the smallest degree is 1, which represent all these leaves
#         for i in range(n):
#             if indegree[i] == 1:
#                 queue.append(i)
#         while queue:
#             path = []
#             #standard BFS using deque
#             for _ in range(len(queue)):
#                 vertex = queue.popleft()
#                 path.append(vertex)
#                 for neigh in graph[vertex]:
#                     indegree[neigh] -=1
#                     if indegree[neigh] == 1:
#                         queue.append(neigh)
#         return path
#
# s = Solution()
# print(s.findMinHeightTrees(6,[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))