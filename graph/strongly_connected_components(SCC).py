from collections import defaultdict, deque
import sys


class Graph:
    def __init__(self, no_vert):
        self.V = no_vert
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)


    def DFS_findOrder(self, u, color, stack):
        color[u] = "grey"
        for v in self.graph[u]:
            if(color[v]=="white"):
                self.DFS_findOrder(v, color, stack)

        color[u] = "black"
        stack.append(u)

    def DFS_util(self, reversed_graph, u, visited, components):
        visited[u] = True
        components.add(u)

        for v in reversed_graph[u]:
            if(visited[v]==False):
                self.DFS_util(reversed_graph, v, visited, components)

    def getTranspose(self):
        gr = Graph(self.V)

        for i in range(self.V):
            for j in self.graph[i]:
                gr.add_edge(j, i)

        return gr.graph

    def findStronglyConnectedComponents(self):
        """
        Steps:
        1. Sort the nodes based on the Finishing time
        2. Reverse the node
        3. Run DFS in sequence of the sorted nodes and add its path
        4. This path is the collection. here we checked path from u->v and v->u by reversing

        Time Complexity: O(E+V)
        :return: list of connected components. A component is a collection of node from where each node can be visited from each
        """
        color = ["white"]*self.V
        stack  = deque()

        for i in range(1, self.V):
            if(color[i]=="white"):
                self.DFS_findOrder(i, color, stack)

        reversed_graph = self.getTranspose()
        visited = [False]*self.V

        ans = [0]*(self.V-1)
        result = []

        while stack:
            components = set()
            item = stack.pop()
            if(visited[item]==False):
                self.DFS_util(reversed_graph, item, visited, components)

            if(len(components)>1):
                result.append(components)

        return result


if __name__=="__main__":
    n, m = map(int, sys.stdin.readline().split())

    graph = Graph(n+1)

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph.add_edge(u, v)

    print(*graph.findStronglyConnectedComponents())

