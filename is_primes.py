from typing import List
def is_primes(arr: List):
    size = len(arr)
    result = [True] * size

    for i in range(0, size//2 + 1):
        if result[i]:
            j = i + arr[i]
            while j < size:
                result[j] = False
                j += arr[i]

    return [n for b, n in zip(result, arr) if b]


test_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

res = is_primes(test_list)
print(res)