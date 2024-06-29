from copy import copy


def matrixRotation(matrix, r):
    # Write your code here
    rows = len(matrix)
    cols = len(matrix[0])
    left = 0
    right = cols - 1
    top = 0
    bottom = rows - 1

    while top < bottom and left < right:
        perimeter = ((right - left) + (bottom - top)) * 2
        no_rotations = r % perimeter

        for _ in range(no_rotations):
            first = matrix[top][left]

            #top
            for i in range(left, right):
                matrix[top][i] = str(matrix[top][i + 1])
            #right
            for i in range(top, bottom):
                matrix[i][right] = str(matrix[i + 1][right])
            #bottom
            for i in range(right, left, -1):
                matrix[bottom][i] = str(matrix[bottom][i - 1])
            #left
            for i in range(bottom, top, -1):
                matrix[i][left] = str(matrix[i - 1][left])

            matrix[top + 1][left] = str(first)

        left += 1
        right -= 1
        top += 1
        bottom -= 1

    for m in matrix:
        print(*m, sep=' ')
