

def chocolateFeast(n, c, m):
    initial_bars = n // c
    wraps_remaining = 0

    count = initial_bars
    while initial_bars + wraps_remaining >= m:
        total_wraps = initial_bars + wraps_remaining
        wraps_remaining = total_wraps % m
        initial_bars = total_wraps // m
        count += initial_bars

    return count


n = 15
c = 3
m = 2

n = 10
c = 2
m = 5

n = 12
c = 4
m = 4

n = 6
c = 2
m = 2

print(chocolateFeast(n, c, m))

