from typing import List


def sudoku(puzzle) -> bool:
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1 and solve(r, c, puzzle):
                return True
    return False
def solve(r: int, c: int, puzzle: List[List]) -> bool:

    if c == len(puzzle[0]):
        r += 1
        c = 0

    if r == len(puzzle):
        return True

    for i in range(1, 10):
        if is_valid(i, r, c, puzzle):
            puzzle[r][c] = i
            if solve(r, c + 1, puzzle):
                return True

        puzzle[r][c] = -1

    return False


def is_valid(num: int, r: int, c: int, puzzle: int) -> bool:
    if num in puzzle[r]:
        return False

    if num in [puzzle[row][c] for row in range(0, 9)]:
        return False

    row_start = (r // 3) * 3
    col_start = (c // 3) * 3

    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if num == puzzle[i][j]:
                return False

    return True


puzzle = [
            [3, 9, -1, -1, 5, -1, -1, -1, -1],
            [-1, -1, -1, 2, -1, -1, -1, -1, 5],
            [-1, -1, -1, 7, 1, 9, -1, 8, -1],
            [-1, 5, -1, -1, 6, 8, -1, -1, -1],
            [2, -1, 6, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [5, -1, -1, -1, -1, -1, -1, -1, -1],
            [6, 7, -1, 1, -1, 5, -1, 4, -1],
            [1, -1, 9, -1, -1, -1, 2, -1, -1]

        ]

res = sudoku(puzzle)
print(res)