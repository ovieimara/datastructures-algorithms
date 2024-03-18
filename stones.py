from typing import Set, List

def stones(n, a, b):
    mini = (n - 1) * min(a, b)
    maxi = (n - 1) * max(a, b)

    result = []
    for i in range(mini, maxi + 1, abs(b - a) or a):
        result.append(i)

    return result


# def count_stones(n, a, b, i, j, series, result: List, memo = {}):
#     key = str(i) + ' ' + str(j)
#     if memo.get(key):
#         return memo.get(key)
#     print(key, memo)
#
#     if j >= n:
#         result.append(series)
#         # print(result)
#         return []
#
#     left = count_stones(n, a, b, i+a, j+1, series + [i], result, memo)
#     right = count_stones(n, a, b, i+b, j+1, series + [i], result, memo)
#     left.extend(right)
#     memo[key] = left
#     return left

n = 3
a = 1
b = 2
arr = [1, 2]
# n = 4
# a = 10
# b = 100
#
n = 2
a = 2
b = 3
arr = [2, 3]

# n = 4
# a = 8
# b = 16

# print(stones(n, a, b))
arr = [10, 20, 30]
n = 4
a = 10
b = 100
result = []
series=[]
idx = 0
print(count_stones(arr, n, series, idx, a, b, result))