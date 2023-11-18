def birthday(s, d, m):
    # Write your code here
    return getWays2(s, d, m)

'O(n^2) time, O(1) space'
def getWays(s, d, m):
    ways = 0
    size = len(s)
    for i in range(size - m + 1):
        sqrs = sum(s[i: i + m])
        if sqrs == d:
            ways += 1

    return ways

'O(n) time, O(1) space'
def getWays2(s, d, m):
    size = len(s)
    day = sum(s[0:m])
    ways = int(day == d)

    for i in range(1, size - m + 1):
        print(day)
        prev = s[i - 1]
        nxt = s[i + m - 1]
        day = (day - prev) + nxt
        ways += int(day == d)
    print(ways)
    return ways

s = [1, 2, 1, 3, 2]
d = 3
m = 2

birthday(s, d, m)