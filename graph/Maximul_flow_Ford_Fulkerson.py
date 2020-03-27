class Graph:
    def __init__(self,graph):
        self.graph = graph
        self.ROW = len(graph)

    # BFS to find a path from source to sink
    ''' This won't return the same path as residual flow value is checked'''
    def BFS(self, source, sink, parent):
        visited = [False]*self.ROW
        queue = []

        visited[source] = True
        queue.append(source)

        while queue:
            u = queue.pop()
            for idx, val in enumerate(self.graph[u]):
                if (visited[idx]==False and val>0):
                    visited[idx] = True
                    queue.append(idx)
                    parent[idx] = u


        return True if visited[sink] else False

    def FORD_FULKERSON(self, source, sink):
        '''
        # Return the Maximum flow in a Graph
        Steps:
        1. Initialize with a zero flow.
        2. Find a augmenting path. An augmenting path is Non full Forward flow and Backward flow with non zero forward flow
        3. Add the lowest flow of the path.
        4. Subtract from the forward flow and add to the backward flow

        Time Complexity: O(VE^2)
        '''
        parent = [-1]*self.ROW

        max_flow = 0

        # Find maximum flow through the path
        while self.BFS(source, sink, parent):
            path_flow = float("inf")
            s = sink
            while(s!=source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow+=path_flow

            # Update the augmented path
            v = sink
            while(v!=source):
                u = parent[v]
                self.graph[u][v] = self.graph[u][v] - path_flow
                self.graph[v][u] = self.graph[v][u] + path_flow
                v = u

        return max_flow


graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0;
sink = 5

print("The maximum possible flow is %d " % g.FORD_FULKERSON(source, sink))

# This code is contributed by Neelam Yadav

