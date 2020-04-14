def gameOfLife(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])

    def lifeCounts(i, j):
        cnt = 0
        for r in range(max(i - 1, 0), min(i + 1, row_len-1)+1):
            for c in range(max(j-1, 0), min(j+1, col_len-1)+1):
                cnt+= matrix[r][c] & 1

        cnt -= matrix[i][j] & 1
        return cnt

    # lifeCounts(0,0)
    for i in range(row_len):
        for j in range(col_len):
            lives = lifeCounts(i, j)

            # In the beginning every second bit is 0. 00 or 01
            if matrix[i][j]==1 and lives >=2 and lives<=3:
                # Survive next
                matrix[i][j] = 3 # 01 --> 11

            if matrix[i][j]==0 and lives==3:
                # Survive next
                matrix[i][j] = 2 # 00 --> 01

    for i in range(row_len):
        for j in range(col_len):
            matrix[i][j] >>= 1 # Get the 2nd State


    # return matrix


matrix = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
gameOfLife(matrix)
print(matrix)




