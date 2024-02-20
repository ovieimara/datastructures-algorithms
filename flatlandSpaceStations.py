def flatlandSpaceStations(n, c):
    m = len(c)
    if n == m:
        return 0

    c.sort()
    left = c[0] - 0
    for i in range(1, m):
        left = max(left, (c[i] - c[i - 1]) // 2)

    right = max(left, n - 1 - c[m - 1])

    return right