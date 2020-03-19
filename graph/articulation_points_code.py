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
        """
        We visit the graph in DFS tree
        We keep track the Discovery time and
        The time of the subtree(v) from which we can reach the ancestor in shortest time
        If we get a edge u-v where we get low[v] > disc[u] means there is no backedge which connects the subtree with one of its ancesotor

        Time Complexity: O(V+E) -> DFS complexity
        :return: nodes removal of which divide the graph into two parts
        """
        start_node = 0
        self.starting_node = start_node
        self.time = 0
        self.visited = [False for _ in range(self.no_nodes)]
        self.parent = [-1 for _ in range(self.no_nodes)]
        self._find_articulation_nodes_util(u=self.starting_node)

        return self.articulation_nodes


    def _find_articulation_nodes_util(self, u):
        self.time = self.time+1
        self.d[u] =  self.time
        self.low[u] = self.time
        self.visited[u] = True

        no_of_child = 0

        for v in self.graph[u]:
            if(v == self.parent[u]):
                continue

            elif(self.visited[v]): #Back Edge
                self.low[u] = min(self.low[u], self.d[v])

            elif(not self.visited[v]): #Tree Edge
                self.parent[v] = u
                self._find_articulation_nodes_util(v)

                self.low[u] = min(self.low[u], self.low[v])
                if self.d[u] <= self.low[v] and u != self.starting_node:
                    self.articulation_nodes.append(u)

                no_of_child+=1

            # Handle the root edge
            if(no_of_child>1 and u == self.starting_node):
                self.articulation_nodes.append(u)


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