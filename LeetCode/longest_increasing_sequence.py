def dfs(matrix, vis, i, j, ar):
    dir = [[0,1],[1,0],[-1,0],[0,-1]]
    r = len(matrix)
    c = len(matrix[0])

    vis[i][j] = True
    ar.append(matrix[i][j])
    print(ar)
    i = 0
    for d in dir:
        i+=1
        x, y = i+d[0], j+d[1]
        if(x>=0 and x<r and y>=0 and y<c and vis[x][y]==False):
            if(matrix[x][y]>matrix[i][j]):
                dfs(matrix, vis, x, y, ar)
            else:
                ar = []
                vis[x][y] = True

    print()
    return ar




def longestIncreasingPath(matrix):
    r = len(matrix)
    c = len(matrix[0])

    vis = [[False for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            print("res", dfs(matrix, vis, i, j, []))
            vis = [[False for _ in range(c)] for _ in range(r)]


matrix = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

longestIncreasingPath(matrix)
