def surfaceArea(A):
    cols = len(A[0])

    total = 0
    for c in range(0, cols):
        if c == 0:
            total += front(A, c)
        else:
            total += front_face(A, c)

        total += top_bottom(A)
        total += sides(A, c)
        total += rear(A, c)

        total += top_bottom(A)

    return total


def front(A, c):
    rows = len(A)
    cols = len(A[0])

    total = 0
    for i in range(rows):
        total += A[i][c]
    return total

def front_face(A, col):
    rows = len(A)
    # cols = len(A[0])

    total = 0
    for i in range(rows):
        total += abs(A[i][col] - A[i][col - 1])
    print(total, col)

    return total

def top_bottom(A):
    rows = len(A)
    # cols = len(A[0])
    return rows

def sides(A, col):
    rows = len(A)
    total = 0

    for i in range(rows):
        if i == 0 or i == rows - 1:
            total += A[i][col]

        if i > 0 or (i == rows - 1 and i > 0):
            total += abs(A[i-1][col] - A[i][col])

        if i == rows - 1 and i == 0:
            total += A[i][col]

    return total

def rear(A, col):
    cols = len(A[0])

    if col == cols - 1:
        return front(A, col)
    else:
        return 0


A = [[1]]
A = [
        [1, 3, 4],
        [2, 2, 3],
        [1, 2, 4]
    ]
# A = [[91, 80, 7, 41, 36, 11, 48, 57, 40, 43]]
res = surfaceArea(A)
print(res)
print(A[0:][0])
