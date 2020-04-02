def bfs(n, m, edges, s):
    # initializing graph
    graph = {i: [] for i in range(1, n + 1)}
    # taking the edges input
    visited, queue, level = [False] * (n + 1), [], [0] * (n + 1)
    # push start node
    queue.append(s)
    visited[s] = True
    level[s] = 0
    # iterate until queue is empty
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if visited[neighbor] == False:
                level[neighbor] = level[vertex] + 6
                queue.append(neighbor)
                visited[neighbor] = True

    return level


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n, m = map(int, input().split())
        edges = []
        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())
        result = bfs(n,m,edges,s)
        print(result)