class Graph:
    def __init__(self, nodes):
        self.graph = {i:[] for i in range(1,nodes+2)}
        self.nodes = nodes

    def add_adges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def minimumVertexCover(self):
        cache = [[-1] * 5 for _ in range(self.nodes + 2)]
        parent = [None] * (self.nodes + 2)

        def func(u, flag):
            if (len(self.graph[u]) == 0):
                return 0

            if cache[u][flag] != -1:
                return cache[u][flag]

            sum = 0
            for v in self.graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    if flag == 0:
                        sum += func(v, 1)
                    else:
                        sum += min(func(v, 0), func(v, 1))

            cache[u][flag] = flag + sum
            return cache[u][flag]

        ans = min(func(1, 0), func(1, 1))
        return ans


if __name__=="__main__":
    while True:
        N = int(input())
        if N==0:
            break
        g = Graph(N)

        for i in range(1,N+1):
            lis = list(map(int, input().split()))
            l = len(lis)
            for j in range(1,l):
                g.add_adges(i, lis[j])

        print(g.graph)

        print(g.minimumVertexCover())
