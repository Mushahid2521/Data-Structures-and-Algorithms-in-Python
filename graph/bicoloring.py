def bfs(n, graph, s):
    visited, queue, color = [False]*(n+1), [], [-1 for _ in range(n)]
    visited[s] = True
    queue.append(s)
    color[s] = 0

    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if visited[v]==False:
                color[v] = 0 if color[u] else 1
                visited[v] = True
                queue.append(v)
            elif color[u] == color[v]:
                return False

    return True

while True:
    n = int(input())
    if(n==0):
        break
    l = int(input())
    graph = {i:[] for i in range(0,n)}
    for _ in range(l):
        u, v = map(int, input().rstrip().split())
        graph[u].append(v)
        graph[v].append(u)

    result = bfs(n, graph, 0)
    if result:
        print("BICOLORABLE.")
    else:
        print("NOT BICOLORABLE.")
