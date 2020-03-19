import sys
"""
This type of algorithm is known as: All Pairs Shortest Path (Multiple query of shortest path in a Weighted Graph)
"""

def floyd_warshall(matrix, n):
    """
    :param matrix: Contains cost as Adjacency list. If there is no connaction, INF distance is ste
    :param n: Number of Nodes
    :return: Return the new matrix containing paths

    Steps:
    1. Keeping K in middle find if there is a shorter distance
    2. Update if there is
    """
    next = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if(matrix[i][k]+matrix[k][j] < matrix[i][j]):
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    next[i][j] = next[i][k]

    return matrix


def find_path(i,j, next):
    path = [i]
    while i!=j:
        i = next[i][j]
        path.append(i)

    return path

if __name__=="__main__":
    n, m = map(int, input().split())
    matrix = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        matrix[u][v] = w

    t = int(input())

    matrix = floyd_warshall(matrix, n)
    for _ in range(t):
        s, f = map(int, input().split())
        if(s==f):
            print(0)
        elif(matrix[s][f]==sys.maxsize):
            print(-1)
        else:
            print(matrix[s][f])

