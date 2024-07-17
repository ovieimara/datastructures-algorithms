from typing import List


def rotateLeft(d, arr: List):
    # Write your code here
    arr_copy = arr.copy()

    for i, num in enumerate(arr):
        arr_copy[i - d] = num

    return arr_copy


array = [1, 2, 3, 4, 5]
d = 4
res = rotateLeft(d, array)
print(res)