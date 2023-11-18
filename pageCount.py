def pageCount(n, p):
    # Write your code here
    front = back = ''

    if p % 2 == 0 and n % 2 > 0:
        back = (n - 1 - p) // 2

    elif p % 2 > 0 and n % 2 == 0:
        back = (n + 1 - p) // 2

    else:
        back = (n - p) // 2

    if p % 2 == 0:
        front = p // 2
    elif p % 2 > 0:
        front = (p - 1) // 2

    return min(front, back)

n = 6
p = 2

res = pageCount(n, p)