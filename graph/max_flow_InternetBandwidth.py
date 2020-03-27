class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def BFS(self, source, sink, parent):
        visited = [False]*self.ROW
        queue = []

        visited[source] = True
        queue.append(source)

        while queue:
            u = queue.pop()
            for idx, val in enumerate(self.graph[u]):
                if(visited[idx]==False and val>0):
                    visited[idx] = True
                    parent[idx] = u
                    queue.append(idx)

        return True if visited[sink] else False

    def Ford_Fulkerson(self, source, sink):
        parent = [-1]*self.ROW
        max_flow = 0

        while self.BFS(source, sink, parent):
            path_flow = float("inf")

            s = sink
            while(s!=source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow+=path_flow

            v = sink
            while(v!=source):
                u = parent[v]
                self.graph[u][v] = self.graph[u][v] - path_flow
                self.graph[v][u] = self.graph[v][u] + path_flow
                v = u

        return max_flow


if __name__=="__main__":
    T = int(input())

    for i in range(1,T+1):
        N = int(input())

        graph = [[0 for _ in range(N)] for _ in range(N)]

        G = Graph(graph)

        source, sink, c = map(int, input().split())

        for j in range(c):
            u, v, w = map(int, input().split())
            G.add_edge(u-1, v-1, w)

        res = G.Ford_Fulkerson(source-1, sink-1)

        print(f"Case {i}: {res}")
