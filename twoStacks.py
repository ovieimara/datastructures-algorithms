from typing import List, Dict


def twoStacks(maxSum, a, b):
    # Write your code here
    # a.sort()
    # b.sort()
    memo = {}
    res = []
    return removeFromStack(maxSum, a, b)
    # removeFromStack2(maxSum, 0, 0, 0, 0, a, b, memo, res)
    print(res)


def removeFromStack(maxSum, a, b):
    i = j = 0
    cum_sum = 0
    count = 0

    while i < len(a) and cum_sum <= maxSum:
        cum_sum += a[i]
        i += 1

    selections = count = i
    i -= 1

    while j < len(b) and i >= 0:
        if cum_sum + b[j] <= maxSum:
            cum_sum += b[j]
            j += 1
            count += 1
            selections = max(selections, count)

        elif i >= 0:
            cum_sum -= a[i]
            i -= 1
            count -= 1

    return selections


a = [4, 2, 4, 6, 1]
b = [2, 1, 8, 5]
maxSum = 10

res = twoStacks(maxSum, a, b)
print(res)