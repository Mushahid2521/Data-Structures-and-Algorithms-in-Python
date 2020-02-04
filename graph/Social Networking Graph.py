def bfs(n, graph, source, dis):
    visited, queue, level = [False]*(n+1), [], [0]*(n+1)
    visited[source] = True
    queue.append(source)
    level[source] = 0

    count = 0
    while  queue:
        u = queue.pop(0)
        for v in graph[u]:
            if(visited[v]==False):
                level[v] = level[u] + 1
                if(level[v]==dis):
                    count+=1
                visited[v] = True
                queue.append(v)

    return count

if __name__=='__main__':
    n, m = map(int, input().rstrip().split())
    graph = {i:[] for i in range(0,n+1)}
    for _ in range(m):
        u, v = map(int, input().rstrip().split())
        graph[u].append(v)
        graph[v].append(u)

    q = int(input())
    for _ in range(q):
        s, t = map(int, input().rstrip().split())
        r = bfs(n, graph, s, t)
        print(r)