# https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn


def sudukuValidate(grid):
    # Unit Check
    def unit_check(data):
        cache = [0]*10
        for val in data:
            if val==".":
                continue
            cache[int(val)]+=1
            if cache[int(val)] > 1:
                return False
        return True

    # Square Check
    def square_check():
        for i in (0,3,6):
            for j in (0,3,6):
                square = [grid[x][z] for x in range(i, i + 3) for z in range(j, j + 3)]
                if not unit_check(square):
                    return False

        return True

    def row_check():
        for i in range(9):
            row = [grid[i][j] for j in range(9)]
            if not unit_check(row):
                return False
        return True

    def column_check():
        for i in range(9):
            column = [grid[j][i] for j in range(9)]
            if not unit_check(column):
                return False
        return True

    print(column_check())
    #return True if square_check() and row_check() and column_check() else False




print(sudukuValidate(
    [[".",".","4",".",".",".","6","3","."],
     [".",".",".",".",".",".",".",".","."],
     ["5",".",".",".",".",".",".","9","."],
     [".",".",".","5","6",".",".",".","."],
     ["4",".","3",".",".",".",".",".","1"],
     [".",".",".","7",".",".",".",".","."],
     [".",".",".","5",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."]]))


