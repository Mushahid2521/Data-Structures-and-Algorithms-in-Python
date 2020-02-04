class Graph:
    def __init__(self, n_vertices):
        self.graph = []
        self.n_vertices = n_vertices
        # Following used by Disjoint set union
        self.parent = [i for i in range(n_vertices+1)]
        self.rank = [0 for i in range(n_vertices+1)]

    def add_edge(self, ls):
        self.graph.append(ls)

    # The following two functions is used for Disjoint set union Data Structure.
    # It can be further optimized by Union by Rank or Path Compression technique
    def find_parent(self, i):
        if self.parent[i] == i:
            return i
        return self.find_parent(self.parent[i])

    def union(self, x, y):
        xset = self.find_parent(x)
        yset = self.find_parent(y)

        # Attach smaller rank tree under the root of high rank tree (Union by Rank)
        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        # If rank are same then add anyone of it and increase its rank
        else:
            self.parent[xset] = yset
            self.rank[yset]+=1

    def kruskal(self):
        '''
        Kruskal is an algorithm to find the minimum spanning tree.

        # Complexity: O(ElogV) or O(ElogV). Sorting the edges take O(ElogE) then we iterate over
                      each edges to find union and find, which takes O(logV) in total O(ElogV). So O(ElogV + ElogV)

        Steps:
            1. Sort the edges with the weights.
            2. Check if the new node creates a cycle in the so far created tree, if not add the edge into the tree
                For this it uses the Disjoint set union Data Structure
        '''
        e = 0
        i = 0
        self.graph.sort(key= lambda x : x[2])
        total_cost = 0
        result = []
        # Total edge will be nodes-1 for mst
        while e < self.n_vertices-1:
            u, v, w = self.graph[i]
            i+=1

            uset = self.find_parent(u)
            vset = self.find_parent(v)
            if(uset!=vset):
                total_cost += w
                result.append([u,v,w])
                self.union(u,v)
                e+=1


        return total_cost


if __name__ == '__main__':

    g_nodes, g_edges = map(int, input().rstrip().split())

    g = Graph(g_nodes)

    for i in range(g_edges):
        ls = list(map(int, input().split()))
        g.add_edge(ls)


    res = g.kruskal()
    print(res)