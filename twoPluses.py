from collections import defaultdict

from typing import List, Tuple, Set, Dict
import heapq
from functools import reduce

def twoPluses(grid):
    # Write your code here
    grid = processGrid(grid)
    GOOD = 'G'
    good = 'g'
    result = 0
    rows = len(grid)
    cols = len(grid[0])

    for n in range(1, rows):
        for m in range(1, cols):
            r = 0
            print(r, n, m)
            while grid[n + r][m] == GOOD and grid[n-r][m] == GOOD and grid[n][m+r] == GOOD and grid[n][m-r] == GOOD:
                grid[n + r][m] = good
                grid[n - r][m] = good
                grid[n][m + r] = good
                grid[n][m - r] = good

                for i in range(1, rows):
                    for j in range(1, cols):
                        x = 0
                        while grid[i + x][j] == GOOD and grid[i - x][j] == GOOD and grid[i][j + x] == GOOD and grid[i][
                            j - x] == GOOD:
                            result = max(result, (4 * r + 1) * (4 * x + 1))
                            x += 1
                # print("result: ", result)
                r += 1

            r = 0
            while grid[n + r][m] == good and grid[n-r][m] == good and grid[n][m+r] == good and grid[n][m-r] == good:
                grid[n + r][m] = GOOD
                grid[n - r][m] = GOOD
                grid[n][m + r] = GOOD
                grid[n][m - r] = GOOD
                r += 1

    return result

def processGrid(grid):
    rows = len(grid)
    cols = len(grid[0])
    grids = []
    grids.append(['O'] * (cols + 2))

    for i in range(rows):
        grids.append(['O'] + list(grid[i]) + ['O'])

    grids.append(['O'] * (cols + 2))

    return grids


grid = [
        "BGBBGB",
        "GGGGGG",
        "BGBBGB",
        "GGGGGG",
        "BGBBGB",
        "BGBBGB"
        ]

grid = [
        "GGGGGG",
        "GBBBGB",
        "GGGGGG",
        "GGBBGB",
        "GGGGGG"
        ]

# grid = [
#         "GGGGGGGGGGGG",
#         "GBGGBBBBBBBG",
#         "GBGGBBBBBBBG",
#         "GGGGGGGGGGGG",
#         "GGGGGGGGGGGG",
#         "GGGGGGGGGGGG",
#         "GGGGGGGGGGGG",
#         "GBGGBBBBBBBG",
#         "GBGGBBBBBBBG",
#         "GBGGBBBBBBBG",
#         "GGGGGGGGGGGG",
#         "GBGGBBBBBBBG"
#     ]
#
# grid = [
#         "BBBGBGBBB",
#         "BBBGBGBBB",
#         "BBBGBGBBB",
#         "GGGGGGGGG",
#         "BBBGBGBBB",
#         "BBBGBGBBB",
#         "GGGGGGGGG",
#         "BBBGBGBBB",
#         "BBBGBGBBB",
#         "BBBGBGBBB"
# ]
res = twoPluses(grid)
print(res)