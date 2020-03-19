from collections import defaultdict

class Graph:
    def __init__(self, no_nodes):
        self.no_nodes = no_nodes
        self.graph = defaultdict(list)
        self.articulation_nodes = []
        self.d = [0 for _ in range(no_nodes)] # Visiting Time
        self.low = [0 for _ in range(no_nodes)]


    def _build_graph(self, edges):
        for pair in edges:
            u, v = pair[0], pair[1]
            self.graph[u].append(v)
            self.graph[v].append(u)

    def _find_critical_nodes(self):
        start_node = 0
        self.starting_node = start_node
        self.time = 0
        self.visited = [False for _ in range(self.no_nodes)]
        self.parent = [-1 for _ in range(self.no_nodes)]
        self._find_articulation_nodes_util(u=self.starting_node)

        print([i for i in range(4)])
        print(self.d)
        print(self.low)
        return self.articulation_nodes


    def _find_articulation_nodes_util(self, u):
        self.time = self.time+1
        self.d[u] =  self.time
        self.low[u] = self.time
        self.visited[u] = True

        for v in self.graph[u]:
            if(self.visited[v]!=True):
                self.parent[v] = u

                self._find_articulation_nodes_util(v)
                self.low[u] = min(self.low[u], self.low[v])

                if(self.low[v]>self.d[u]):
                    self.articulation_nodes.append([u,v])

            elif(v!=self.parent[u]):
                self.low[u] = min(self.low[u], self.d[v])



class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = Graph(n)
        graph._build_graph(connections)
        return graph._find_critical_nodes()


if __name__=="__main__":
    s = Solution()
    print(s.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))

