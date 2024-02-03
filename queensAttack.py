def queensAttack(n, k, r_q, c_q, obstacles):
    obs = convertObstaclesToSet(obstacles)
    squares = []
    attack(n, k, r_q, c_q, obs, squares)
    return len(squares)


def attack(n, k, r_q, c_q, obstacles, squares):
    ''''''
    print(obstacles)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1 ,1), (1, -1)]

    for direction in directions:
        canAttack(r_q, c_q, k, direction, n, obstacles, squares)

def canAttack(r, c, k, direction, n, obstacles, squares):
    x, y = direction
    row, col = r + x, c + y
    while 1 <= row <= n and 1 <= col <= n:

        if k > 0 and (row, col) in obstacles:
            print(row, col)
            break
        squares.append((row, col))
        row, col = row + x, col + y

def convertObstaclesToSet(obstacles):
    # obstacles = set(obstacles)
    result = []
    for r, c in obstacles:
        result.append((r, c))

    return set(result) if result else set()

n = 5
k = 3
r = 4
c = 3

n = 4
k = 0
r = 4
c = 4

n = 1
k = 0
r = 1
c = 1

obstacles = [[5, 5], [4, 2], [2, 3]]
obstacles = []
res = queensAttack(n, k, r, c, obstacles)
print(res)