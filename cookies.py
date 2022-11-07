#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#


def cookies(k, A):
    # Write your code here
    # cookys = sorted(A)
    if not A:
        return -1

    heapq.heapify(A)
    result = getSweetness(A, k)
    return result


def getSweetness(cookys, k):
    count = 0
    while len(cookys) >= 2 and cookys[0] < k:
        first = heapq.heappop(cookys)
        second = heapq.heappop(cookys)
        sweetness = first + (second * 2)
        heapq.heappush(cookys, sweetness)
        count += 1

    return count if cookys[0] >= k else -1


# def getSweetness(cookys, k):
#     count = 0
#     while len(cookys) >= 2 and cookys[0] < k:
#         first = cookys.popleft()
#         second = cookys.popleft()
#         sweetness = first + (second * 2)
#         bisect.insort(cookys, sweetness)
#         count += 1

#     return count if cookys[0] >= k else -1


# def getSweetness(cookys, k, count):
#     if not cookys:
#         return -1
#     if cookys[0] >= k:
#         return count[0]
#     if len(cookys) < 2:
#         return -1

#     count[0] += 1
#     sweetness = cookys[0] + (cookys[1] * 2)
#     bisect.insort(cookys, sweetness)
#     if cookys:
#         cookys.popleft()
#     if cookys:
#         cookys.popleft()
#     return getSweetness(cookys, k, count)



