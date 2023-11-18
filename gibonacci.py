
def gibonacci(n, x, y, memo=None):
    if not memo:
        memo = {}
    if n in memo:
        return memo.get(n)
    if n <= 0:
        return x
    if n == 1:
        return y

    res = gibonacci(n - 1, x, y, memo) - gibonacci(n-2, x, y, memo)
    memo[n] = res
    return res

# val = gibonacci(0, 0, 1)
# val = gibonacci(1, 0, 1)
# val = gibonacci(2, 0, 1)
# val = gibonacci(3, 0, 1)
# val = gibonacci(4, 0, 1)
# val = gibonacci(4, 1, 2)
# val = gibonacci(4, -5, 2)
# val = gibonacci(4, -5, -2)
# val = gibonacci(-4, -5, 2)
val = gibonacci(400, -5, 2)


print(val)
