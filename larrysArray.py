from typing import List, Set
from collections import deque

def larrysArray(A):
    count = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                count += 1

    return 'YES' if count % 2 == 0 else 'NO'

# def larrysArray(A):
#     # print(A)
#     # arr = A
#     size = len(A)
#     store = []
#     visited = set()
#     sorted_arr = sorted(A)
#     # print('sorted_arr: ', sorted_arr)
#     if A == sorted_arr:
#         return True
#     processSequence(A, store, visited)
#
#     while len(store) > 0:
#         perm, seq = store.pop()
#         # print('sex: ', seq, perm)
#         new_seq = swap(perm, seq)
#         if new_seq == sorted_arr:
#             return "YES"
#         processSequence(new_seq, store, visited)
#         size -= 1
#     return "NO"

def swap(perm: List, seq) -> List:
    start, end = perm
    arr = seq[start: end]
    arr[0], arr[-1] = arr[-1], arr[0]
    arr[0], arr[1] = arr[1], arr[0]

    return seq[:start] + arr + seq[end:]

def processSequence(seq: List, store: List, visited: Set) -> None:
    prev_val = 0
    j = 0
    prev = 0
    while j < len(seq) and seq[j] == prev+1:
        prev = seq[j]
        j += 1
    # print('seq: ', seq)
    perms = []
    # if seq[j:]:
    min_val = min(seq[j:])
    index = seq.index(min_val)
    max_val = max(seq[j:])
    perm_1 = seq[index - 2: index+1]
    perm_2 = seq[index-1: index+2]
    # print(perm_2, perm_1)
    perm = ''
    if len(perm_1) == 3 and len(perm_2) == 3:
        perm = (perm_1, (index-2, index+1)) if perm_1[0] > perm_2[0] else (perm_2, (index-1, index+2))
    else:
        perm = (perm_1, (index-2, index+1)) if len(perm_1) == 3 else (perm_2, (index-1, index+2))

    if tuple(perm[0]) not in visited and len(perm[0]) == 3:
        store.append((perm[1], seq))
        visited.add(tuple(perm[0]))



# def processSequence(seq: List, store: List, visited: Set) -> None:
#     for i in range(len(seq) - 2):
#         perm = seq[i: i + 3]
#         # if len(perm) == 3 and perm[1] == perm[0] + 1 and perm[2] == perm[0] + 2:
#         #     continue
#         if tuple(perm) in visited:
#             continue
#         store.append(((i, i+3), seq))
#         visited.add(tuple(perm))


A = [1, 6, 5, 2, 4, 3]
# A = [3, 1, 2]
# A = [1, 3, 4, 2]
# A = [1, 2, 3, 5, 4]

res = larrysArray(A)
print(res)