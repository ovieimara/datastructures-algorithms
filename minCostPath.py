def minCostPath(matrix, n, m):
    i = j = 0
    cost = 0
    return mincost_path(matrix, i, j, n, m, cost)

def mincost_path(matrix, i, j, n, m, cost):
    if i == n or j == m:
        return float("inf")

    current_cost = cost + matrix[i][j]
    if i == n - 1 and j == m -1 :
        return current_cost

    # print(current_cost)

    return min(mincost_path(matrix, i + 1, j, n, m, current_cost), mincost_path(matrix, i, j+1, n, m, current_cost))

matrix = [[3, 12, 4, 7, 10],
          [6, 8, 15, 11, 4],
          [19, 5, 14, 32, 21],
          [1, 20, 2, 9, 7]
          ]

result = minCostPath(matrix, 4, 5)
print(result)