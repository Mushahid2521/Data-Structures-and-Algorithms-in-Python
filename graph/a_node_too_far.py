from collections import defaultdict
def bfs(graph, s, t):
    n = 10000
    # visited, queue, level = [False for _ in range(n+1)], [], [0 for _ in range(n+1)]
    visited, queue, level = [False] * (n + 1), [], [0] * (n + 1)
    # push start node
    queue.append(s)
    visited[s] = True
    level[s] = 0
    # iterate until queue is empty
    while queue:
        # pop the first element
        vertex = queue.pop(0)
        # iterate by its neighbors
        for neighbor in graph[vertex]:
            # exclude if  visited
            if visited[neighbor] == False:
                # update the label ot depth
                level[neighbor] = level[vertex] + 1
                queue.append(neighbor)
                visited[neighbor] = True

    cnt = 0
    for v in level:
        if v>t:
            cnt+=1
    return cnt

if __name__== '__main__':
    while True:
        case = 1
        l = int(input())
        if(l==0):
            break
        n = 10000
        graph = {i:[] for i in range(n)}

        for _ in range(l):
            u, v = map(int, input().rstrip().split(" "))
            graph[u].append(v)
            graph[v].append(u)

        while True:
            s, t = map(int, input().rstrip().split())
            if(s==t==0):
                break
            res = bfs(graph, s, t)
            print(f"Case {case}: {res} nodes not reachable from node {s} with TTL = {t}.")
            case+=1


'''
16
10 15
15 20
20 25
10 30
30 47
47 50
25 45
45 65
15 35
35 55
20 40
50 55
35 40
55 60
40 60
60 65
'''