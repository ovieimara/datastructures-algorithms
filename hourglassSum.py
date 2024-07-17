

def hourglassSum(arr):
    # Write your code here
    rows = len(arr)
    cols = len(arr[0])
    directions = [(0, 0), (0, -1), (0, 1), (1, 0), (2, 0), (2, 1), (2, -1)]

    max_sum = float('-inf')
    for r in range(0, (rows-3)+1):
        for c in range(1, cols-1):
            total = 0
            for dirs in directions:
                x, y = dirs
                total += arr[r+x][c+y]
            max_sum = max(max_sum, total)

    return max_sum


array = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0],
        ]

array = [
            [-9, -9, -9, 1, 1, 1],
            [0, -9, 0, 4, 3, 2],
            [-9, -9, -9, 1, 2, 3],
            [0, 0, 8, 6, 6, 0],
            [0, 0, 0, -2, 0, 0],
            [0, 0, 1, 2, 4, 0],
        ]
#
array = [
            [0, -4, -6, 0, -7, -6],
            [-1, -2, -6, -8, -3, -1],
            [-8, -4, -2, -8, -8, -6],
            [-3, -1, -2, -5, -7, -4],
            [-3, -5, -3, -6, -6, -6],
            [-3, -6, 0, -8, -6, -7]
]

res = hourglassSum(array)
print(res)