from typing import List, Set

def absolutePermutation(n, k):
    arr: Set = set(i for i in range(1, n + 1))
    res: List = []

    if k == 0:
        return arr

    for i in range(1, n + 1):
        pos1 = i - k
        pos2 = i + k

        if pos1 in arr:
            res.append(pos1)
            arr.remove(pos1)

        elif pos2 in arr:
            res.append(pos2)
            arr.remove(pos2)

        else:
            return [-1]

    return res

# def absolutePermutation(n, k):
    # arr = [i for i in range(1, n + 1)]
    # rev_arr = [i for i in range(n, 0, -1)]
    #
    # # while arr != rev_arr:
    # is_found = False
    # while True:
    #     if absoluteP(arr, k):
    #         is_found = True
    #         break
    #
    #     arr = nextGreater(arr)
    #     if arr == rev_arr:
    #         break
    #
    # return arr if is_found or absoluteP(arr, k) else [-1]

def absoluteP(arr, k) -> bool:
    for i in range(0, len(arr)):
        if abs(arr[i] - (i+1)) != k:
            return False

    return True
def nextGreater(arr: List):
    i = len(arr) - 2
    while i >= 0 and arr[i] > arr[i+1]:
        i -= 1

    if i < 0:
        return arr

    j = len(arr) - 1
    while j >= 0 and i >= 0 and arr[j] < arr[i]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    new = arr[:i+1] + arr[: i: -1]
    return new

# def absolutePermutation(n, k):
#     arr = [i for i in range(1, n + 1)]
#     size = len(arr)
#     result = [-1] * n
#     for i in range(size):
#         updated = False
#         for j in range(1, size + 1):
#            if abs(arr[i] - j) == k:
#                updated = True
#                result[j - 1] = arr[i]
#         if not updated:
#             return [-1]
#     return result
#
#
#
# def binarySearch(n, left, right, k):
#     print(left, right)
#     if left == right:
#         if abs(n - left) == k:
#             return left
#         else:
#             return -1
#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     # print(abs(n - (mid + 1)))
#     if abs(n - (mid + 1)) == k:
#         return mid + 1
#     elif abs(n - (mid + 1)) < k:
#         right = mid - 1
#         return binarySearch(n, left, right, k)
#     else:
#         left = mid + 1
#         return binarySearch(n, left, right, k)


n = 4
k = 2
n = 2
k = 1
n = 3
k = 0
n = 3
k = 2
n = 9904
k = 6932
# n = 9836
# k = 1699
# n = 9498
# k = 2907
# n = 9548
# k = 0
# n = 9331
# k = 0

res = absolutePermutation(n, k)
print(res)

arr = [2, 1]
k = 1
print(absoluteP(arr, k))