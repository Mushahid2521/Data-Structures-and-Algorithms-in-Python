count = 0
def dfs(matrix, vis, ar):
    '''
    Couldn't Solve
    TODO
    '''
    global count
    r = len(matrix)
    c = len(matrix[0])
    dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    vis[ar[0]][ar[1]] = True
    count+=1
    for d in dir:
        x, y = ar[0] + d[0], ar[1] + d[1]
        if (x >= 0 and x < r and y >= 0 and y < c and vis[x][y] == False):
            if(matrix[x][y]==0):
                vis[x][y] = True
            else:
                return dfs(matrix, vis, [x,y])

    return count

def bfs(matrix, vis, ar):
    queue = []
    r = len(matrix)
    c = len(matrix[0])
    queue.append(ar)
    vis[ar[0]][ar[1]] = True
    dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    global count

    while queue:
        idxs = queue.pop(0)
        count+=1
        for d in dir:
            x,y = idxs[0] + d[0], idxs[1] + d[1]
            if (x >= 0 and x < r and y >= 0 and y < c and vis[x][y] == False):
                if(matrix[x][y]==1):
                    queue.append([x,y])
                    vis[x][y] = True
                else:
                    vis[x][y] = True

    return count


def riverSizes(matrix):
    res = []
    r = len(matrix)
    c = len(matrix[0])
    vis = [[False for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if(matrix[i][j]==1 and vis[i][j]==False):
                res.append(bfs(matrix, vis,[i,j]))
                global count
                count = 0
            else:
                vis[i][j]= True



    return res


# mat = [[1,0,0,1,0],
#        [1,0,1,0,0],
#        [0,0,1,0,1],
#        [1,0,1,0,1],
#        [1,0,1,1,0]]
# mat = [[1,1,1,0,0,1,1,0,1,0]]
mat = [[1,0,0,1,0,1,0,0,1,1,1,0],
       [1,0,1,0,0,1,1,1,1,0,1,0],
       [0,0,1,0,1,1,0,1,0,1,1,1],
       [1,0,1,0,1,1,0,0,0,1,0,0],
       [1,0,1,1,0,0,0,1,1,1,0,1]]
print(riverSizes(mat))