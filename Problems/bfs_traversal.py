t = int(input())
for _ in range(0,t):
    n, m = map(int, input().rstrip().split())
    # initializing graph
    graph = {i:[] for i in range(1,n+1)}
    # taking the edges input
    for _ in range(m):
        u, v = map(int, input().rstrip().split())
        graph[u].append(v)
        graph[v].append(u)

    # initializing necessary variables
    # visited, queue, level = [False for _ in range(n+1)], [], [0 for _ in range(n+1)]
    visited, queue, level = [False]*(n+1), [], [0]*(n+1)
    # push start node
    queue.append(1)
    visited[1] = True
    level[1] = 0
    # iterate until queue is empty
    while queue:
        # pop the first element
        vertex = queue.pop(0)
        # iterate by its neighbors
        for neighbor in graph[vertex]:
            # exclude if  visited
            if visited[neighbor]==False:
                # update the label ot depth
                level[neighbor] = level[vertex]+1
                queue.append(neighbor)
                visited[neighbor] = True

    print(level[n])
