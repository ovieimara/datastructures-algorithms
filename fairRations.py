from typing import List


def fairRations(B):
    count = [0]
    if ration(B, count, 0):
        return str(count[0])
    return 'NO'


def ration(B, count, i):
    if len(B) == 2 and process_even_nos(B) == 1:
        return False
    if len(B) == process_even_nos(B):
        return True
    j = i % len(B)
    if B[j] % 2 != 0:
        give_loaf(B, j, count)

    return ration(B, count, j + 1)


def give_loaf(B: List, i: int, count: List):
    if i == 0 or (i < len(B) - 1 and B[i - 1] % 2 == 0):
        B[i + 1] += 1
    else:
        B[i - 1] += 1

    B[i] += 1
    count[0] += 2


def process_even_nos(arr: List):
    # satisfy = [True if e%2 == 0 else False for e in arr]
    result = 0
    for e in arr:
        if e % 2 == 0:
            result += 1

    return result


B = [2, 3, 4, 5, 6]
B = [4, 5, 6, 7]
print(fairRations(B))