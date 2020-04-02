class Graph:
    def __init__(self, node):
        self.graph = {i:[] for i in range(1,node+1)}
        self.n_edges = node-1

    def addEdges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def minimumVertexCover(self):
        """
        :return: Minimum Number of Nodes to cover all the edges if one edge can see its neighbouring edges
        Steps:
        1. If the node don't has flag then all neighbouring edges must be
        2. If it has then see adding one minimizes or not
        3. Don't visit the parent node if the child is visited. So if u->v. If u, v then don't visit u again for v->u
        4. Base Case: Reaching to a node from where no node is reachable
        """
        cache = [[-1]*5 for _ in range(self.n_edges+2)]
        parent = [None]*(self.n_edges+2)

        def func(u, flag):
            if(len(self.graph[u])==0):
                return 0

            if cache[u][flag]!=-1:
                return cache[u][flag]

            sum = 0
            for v in self.graph[u]:
                if v!=parent[u]:
                    parent[v] = u
                    if flag==0:
                        sum += func(v, 1)
                    else:
                        sum += min(func(v, 0), func(v, 1))

            cache[u][flag] = flag + sum
            return cache[u][flag]

        ans = min(func(1,0), func(1,1))
        return ans


if __name__=="__main__":
    n = int(input())
    g = Graph(n)

    for _ in range(n-1):
        u, v = map(int, input().split())
        g.addEdges(u, v)

    print(g.minimumVertexCover())