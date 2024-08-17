from typing import List, Tuple


def maxSumRectangle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')

    for left in range(cols):
        sums = [0] * rows
        for c in range(left, cols):
            for r in range(rows):
                sums[r] += matrix[r][c]
            max_sum = max(max_sum, maxSubArray(sums))

    return max_sum
def maxSubArray(arr: List) -> int:
    # using kadanes algorithm
    size = len(arr)
    result = [0] * size
    result[0] = arr[0]

    start, end = 0, 0
    max_sum = arr[0]

    for i in range(1, size):
        if arr[i] > (result[i-1] + arr[i]):
            result[i] = arr[i]
            if result[i] > max_sum:
                max_sum = result[i]
                start = i
                end = start

        else:
            result[i] = result[i-1] + arr[i]
            if result[i] > max_sum:
                max_sum = result[i]
                end = i

    return sum(arr[start: end + 1])

arr = [4, -3, 9, 1]
arr = [6, -5, -7, 4]

matrix = [
            [6, -5, -7, 4, -4],
            [-9, 3, -6, 5, 2],
            [-10, 4, 7, -6, 3],
            [-8, 9, -3, 3, -7]
          ]

res = maxSumRectangle(matrix)
print(res)