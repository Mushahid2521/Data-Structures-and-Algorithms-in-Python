def find_parent(parent, i, j):
    print(parent[i][j], i, j)
    if(parent[i][j][0]==i and parent[i][j][1]==j):
        return [i,j]
    return find_parent(parent, parent[i][j][0], parent[i][j][1])


def union(parent, rank , x1, x2, y1, y2):
    xset1, xset2 = find_parent(parent, x1, x2)
    yset1, yset2 = find_parent(parent, y1, y2)

    # Attach smaller rank tree under the root of high rank tree (Union by Rank)
    if rank[xset1][xset2] > rank[yset1][yset2]:
        parent[yset1][yset2] = [xset1, xset2]

    elif rank[xset1][xset2] < rank[yset1][yset2]:
        parent[xset1][xset2] = [yset1,yset2]

    # If rank are same then add anyone of it and increase its rank
    else:
        parent[xset1][xset2] = [yset1,yset2]
        rank[yset1][yset2] += 1

def riverSizes(matrix):
    res = []
    r = len(matrix)
    c = len(matrix[0])
    vis, q, level = [[False for _ in range(c)] for _ in range(r)], [], [[0 for _ in range(c)] for _ in range(r)]
    dir = [[0,1],[1,0],[-1,0],[0,-1]]
    u,v = 0,0
    vis[u][v] = True
    q.append([u,v])
    level[u][v] = 1 if matrix[u][v] else 0

    parent = [[[i, j] for i in range(c)] for j in range(r)]
    rank = [[0 for _ in range(c)] for _ in range(r)]
    s = 0
    while q:
        u, v = q.pop(0)
        n_parent = find_parent(parent, u, v)
        for d in dir:
            x, y = u+d[0], v+d[1]
            if(x>=0 and x<c and y>=0 and y<r and vis[x][y]==False):
                if(matrix[u][v]==matrix[x][y]==1):
                    s+=1
                    union(parent, rank, n_parent[0], n_parent[1], x, y)
                elif(matrix[x][y]==1 and matrix[u][v]==0):
                    res.append(s)
                    s = 0
                elif(matrix[x][y]==0 and matrix[u][v]==1):
                    pass
                
                vis[x][y] = True
                q.append([x,y])
        if(flag==False and matrix[u][v]==1):
            res.append(level[u][v])


    print(level)
    return res


mat = [[1,0,0,1,0],
       [1,0,1,0,0],
       [0,0,1,1,1],
       [1,0,0,0,1],
       [1,0,1,1,0]]
print(riverSizes(mat))