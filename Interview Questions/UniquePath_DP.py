def uniquePath(row, col):
    """
    # Since the robot can only move right and down, when it arrives at a point, it either arrives from left or above.
    #Moreover, we have the base cases dp[0][j] = dp[i][0] = 1 for all valid i and j.
    """
    cache = [[0]*(col+1) for _ in range(row+1)]

    # Filling Base Cases
    for i in range(row):
        cache[i][0] = 1

    for j in range(col):
        cache[0][j] = 1

    for i in range(1,row):
        for j in range(1,col):
            cache[i][j] = cache[i][j-1] + cache[i-1][j]

    return cache[row-1][col-1]


print(uniquePath(3,7))