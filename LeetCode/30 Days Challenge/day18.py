# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3303/
def pathSum(grid):
    row = len(grid)
    col = len(grid[0])
    cache = [[-1]*col for _ in range(row)]

    def dp(i,j):
        if i>=row or j>=col:
            return float("inf")

        if cache[i][j] != -1:
            return cache[i][j]

        if i==row-1 and j==col-1:
            return grid[i][j]

        cache[i][j] = min(grid[i][j]+dp(i+1, j), grid[i][j]+dp(i, j+1))
        return cache[i][j]

    res = dp(0,0)
    return res


print(pathSum([
  [1,2,5],
  [3,2,1],
]))