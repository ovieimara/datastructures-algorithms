import logging
from collections import Counter
from functools import reduce


def formingMagicSquare(s):
    # Write your code here
    magic_squares = generatePossibleMagicSquares()
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]
    return minCost(s, magic_squares)


def minCost(s: list, possibilities: list) -> int:
    def getCost(magic_sqr):
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += (abs(s[i][j] - magic_sqr[i][j]))
        return cost

    costs = list(map(lambda magic_sqr: getCost(magic_sqr), possibilities))
    print(costs)
    return min(costs)


def generatePossibleMagicSquares():
    # 1. create a 3 x 3 matrix
    possibilities = []

    # min_val = min(numbers)
    # max_val = max(numbers)
    # mid_val = (min + max ) / 2

    directions = [[(0, 1), (1, 1), (2, 1)], [(1, 0), (1, 1), (1, 2)]]
    for i in range(len(directions)):
        posibility = [[0 for i in range(3)] for _ in range(3)]
        d = directions[i]
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        row_1, col_1 = d[0]
        row_2, col_2 = d[1]
        row_3, col_3 = d[2]
        posibility[row_1][col_1] = numbers.pop(0)
        posibility[row_2][col_2] = numbers.pop(3)
        max_val = numbers.pop(6)
        posibility[row_3][col_3] = max_val
        if i == 0:
            col_left = col_3 - 1
            col_right = col_3 + 1

            x, y = findSumOfTwoNumbers(numbers, max_val)
            row = row_3

            posibility[row][col_left] = x
            posibility[row][col_right] = y

            posibility[row - 2][col_right] = 15 - int(posibility[row][col_left] + posibility[1][1])
            posibility[row - 2][col_left] = 15 - int(posibility[row][col_right] + posibility[1][1])

            posibility[row - 1][col_left] = 15 - (posibility[row - 2][col_left] + posibility[row][col_left])
            posibility[row - 1][col_right] = 15 - (posibility[row - 2][col_right] + posibility[row][col_right])

            manipulateMatrix(posibility, possibilities)

        if i == 1:
            row_top = row_3 - 1
            row_bottom = row_3 + 1

            x, y = findSumOfTwoNumbers(numbers, max_val)
            col = col_3

            updateSides(posibility, row_top, row_bottom, col, x, y)
            manipulateMatrix(posibility, possibilities)

        return possibilities


def updateSides(posibility, top, bottom, col, x, y):
    posibility[top][col] = y
    posibility[bottom][col] = x

    posibility[bottom][col - 2] = 15 - (posibility[top][col] + posibility[1][1])
    posibility[top][col - 2] = 15 - (posibility[bottom][col] + posibility[1][1])

    posibility[top][col - 1] = 15 - (posibility[top][col] + posibility[top][col - 2])
    posibility[bottom][col - 1] = 15 - (posibility[top][col - 1] + posibility[1][1])
    print(posibility)


def manipulateMatrix(posibility: list, possibilities: list):
    possibilities.append(posibility)
    poss = reversePosibility(posibility)
    poss_2 = posibility[:: -1]
    possibilities.append(poss)
    possibilities.append(poss_2)
    poss_3 = reversePosibility(poss_2)
    possibilities.append(poss_3)


def findSumOfTwoNumbers(numbers: list, number: int):
    store = set()
    target = 15 - number
    for num in numbers:
        val = target - num
        if val in store:
            return val, num
        store.add(num)
    return None


def reversePosibility(posibility):
    possible = posibility[:]
    return list(map(lambda row: row[::-1], possible))

def merge_dictionaries(dict1, dict2):
    # merged_dict = dict1.copy()
    dict1.update(dict2)
    return dict1

def findMultipleValues(counter: dict):
    values = []
    for k, v in counter.items():
        if v > 1:
            [values.append(k) for _ in range(v-1)]

    return values

def findDiff(s):
    set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    set_b = reduce(addSets, map(set, s))
    return list(set_a.difference(set_b))

def addSets(a: set, b: set):
    return a.union(b)

s = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]

magicSquares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

res = formingMagicSquare(s)
print(res)
