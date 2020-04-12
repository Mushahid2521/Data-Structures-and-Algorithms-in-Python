def rotate(matrix):
    l = len(matrix)
    for row in matrix:
        print(row)

    print()
    # Transpose the Matrix
    for i in range(l):
        for j in range(i, l):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        print(row)

    print()
    # Row Reverse
    for i in range(l):
        for j in range(l//2):
            matrix[i][l-j-1], matrix[i][j] = matrix[i][j],  matrix[i][l-j-1]

    for row in matrix:
        print(row)

    return matrix

# Rotate the image 90 degree clockwise
rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])