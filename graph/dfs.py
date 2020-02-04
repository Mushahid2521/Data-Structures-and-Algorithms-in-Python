def dfs(vis, s):
    vis[s] = True
    for u in graph[s]:
        if(vis[u] == False):
            dfs(vis, u)


n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
vis = {i: False for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


s = int(input())
t = 0
dfs(vis, s)

for p in vis.keys():
    if (vis[p] == False):
        t += 1

print(t)

"""
10 10
8 1
8 3
7 4
7 5
2 6
10 7
2 8
10 9
2 10
5 10
2
"""


