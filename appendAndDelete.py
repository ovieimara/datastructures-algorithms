#complexity: Time: O(max(n,m,k)), space = O(max(n, m))
def appendAndDelete(s: str, t: str, k: int):
    n = len(s)
    m = len(t)

    x, y = createArray(s, t, n, m)
    ops = append_delete(x, y, k, max(n, m) - 1, n, m)

    ops += abs(k - ops)

    if ops == k and ''.join(x) == t:
        return 'Yes'

    return 'No'

def append_delete(x: str, y: str, ops: int, i: int, n, m):
    if ops <= 0 or i < 0:
        return 0

    x[i] = y[i]
    if i >= n or i >= m:
        return 1 + append_delete(x, y, ops - 1, i - 1, n, m)

    return 2 + append_delete(x, y, ops - 2, i - 1, n, m)

# def append_delete(x: str, y: str, ops: int, i: int, n, m, total=0):
#     if ops <= 0 or i < 0:
#         return total
#
#     x[i] = y[i]
#     if i >= n or i >= m:
#         return append_delete(x, y, ops - 1, i - 1, n, m, total + 1)
#
#     return append_delete(x, y, ops - 2, i - 1, n, m, total + 2)

def createArray(s: str, t: str, n: int, m: int) -> list:
    length = max(len(s), len(t))
    arr = [''] * length
    arr2 = [''] * length
    for i in range(length):
        if i < n:
            arr[i] = s[i]
        if i < m:
            arr2[i] = t[i]
    return arr, arr2


# o = "hackerhappy"
# p = "hackerrank"
# e = 9

# o = "hackerrank"
# p = "hackerhappy"
# e = 9

# o = "aba"
# p = "aba"
# e = 7

# o = "ashley"
# p = "ash"
# e = 2

# o = "ash"
# p = "ashley"
# e = 2

# o = "aaa"
# p = "a"
# e = 5

# o = "a"
# p = "aaa"
# e = 5
#
# o = "ab"
# p = "bbb"
# e = 5

# o = "abcd"
# p = "efghij"
# e = 10

# o = "abcdef"
# p = "ghij"
# e = 10
#
# o = "a"
# p = "a"
# e = 2
#
# o = "a"
# p = "b"
# e = 1

# o = ""
# p = "aaa"
# e = 3

o = "abcdef"
p = "fedcba"
e = 15

res = appendAndDelete(o, p, e)
print(res)