while True:
    R, C = map(int, input().rstrip().split())
    if(R==C==0):
        break

    graph = [[0 for _ in range(C)] for _ in range(R)]
    rs = int(input())
    for _ in range(rs):
        ls = list(map(int, input().split()))
        i = 2
        for _ in range(ls[1]):
            u, v = ls[0], ls[i]
            graph[u][v] = -1
            i+=1

    r1, c1 = map(int, input().split())
    rn, cn = map(int, input().split())

    # bfs_code
    direction = [[0,1],[1,0],[-1,0],[0,-1]]
    vis, q, level = [[False for _ in range(C)] for _ in range(R)], [], [[0 for _ in range(C)] for _ in range(R)]
    vis[r1][c1] = True
    level[r1][c1] = 0
    q.append([r1, c1])

    while q:
        l = q.pop(0)
        for d in direction:
            tx = l[0] + d[0]
            ty = l[1] + d[1]
            if(tx>=0 and tx<R and ty>=0 and ty<C and vis[tx][ty]==False and graph[tx][ty]!=-1):
                vis[tx][ty] = True
                q.append([tx,ty])
                level[tx][ty] = level[l[0]][l[1]] + 1

    print(level[rn][cn])
