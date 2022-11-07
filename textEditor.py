# def simpleTextEditor(S, ops, stack, count):
#     opsArr = ops.split()
#     # print(opsArr)
#     if stack:
#         S = stack[-1]
#     if opsArr[0] == '1':
#         S += opsArr[1]
#         stack.append(S)
#     elif opsArr[0] == '2':
#         if len(opsArr) > 1 and opsArr[1] != '':
#             S = S[:len(S) - int(opsArr[1])]
#             stack.append(S)
#     elif opsArr[0] == '3':
#         if len(opsArr) > 1 and opsArr[1] != '':
#             print(S[int(opsArr[1]) - 1])
#     elif opsArr[0] == '4':
#         if stack:
#             S = stack.pop()


# !/bin/python3

import math
import os
import random
import re
import sys






#     # !/bin/python3
#
#     import math
#     import os
#     import random
#     import re
#     import sys
#
#
#     #
#     # Complete the 'truckTour' function below.
#     #
#     # The function is expected to return an INTEGER.
#     # The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#     #
#
#     def truckTour(petrolpumps):
#         # Write your code here
#         minIdx = 0
#         fuel = petrolpumps[0][0]
#         distance = petrolpumps[0][1]
#         minFuel = float('inf')
#         size = len(petrolpumps)
#         for i in range(1, size):
#             idx = i % size
#             pump = petrolpumps[idx]
#             f, d = pump
#             fuel -= distance
#             if minFuel > fuel:
#                 minFuel = fuel
#                 minIdx = idx
#
#             fuel += f
#             distance = d
#
#         return minIdx
#
#
# def pairs(k, arr):
#     # Write your code here
#     size = len(arr)
#     diff = 0
#     store = storeDict(arr)
#
#     for i in range(size):
#         if arr[i] + k in store:
#             diff += 1
#
#     return diff
#
#
# def storeDict(arr):
#     store = set()
#     for a in arr:
#         store.add(a)
#
#     return store

# def gibonacci(n, x, y):
#     # base case when n is 0
#     if n == 0:
#         return x
#     # base case when n is 1
#     if n == 1:
#         return y
#
#     return gibonacci(n - 1, x, y) - gibonacci(n - 2, x, y)
#
# val = gibonacci(30, 1, 0)
#
# print(val)

# # def updateArray(arr):
# #     res = [arr[i] for i in range(len(arr)) if arr[i] > 0]
# #     print(res)
# #     return res
# #
# #
# # def lambdaMap(arr):
# #     ans = map(
# #
# # # Complete the lambda function below.  It begins in the non-alterable code above
# # lambda a : [num ** 2 for num in updateArray(a) ]
# #
# # , arr)
# #
# #     return  ans
# #
# # arr = [[-1, 1, 2, -2, 6], [3, 4, -5]]
# # val = lambdaMap(arr)
# print(list(val))


def reversed_args(f):
    def wrapper(*args):
        new_args = args[: : -1]
        return f(new_args)
    return wrapper


k = f(2,3)
val = reversed_args(k)
print(val)
