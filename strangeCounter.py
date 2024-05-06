def strangeCounter(t):
    # Write your code here
    i = cycle(t)
    value = i + 2

    return value - (t - i)

    # return binaryCycle(t, i, i + value - 1, value, 1)


def binaryCycle(t, start, end, start_value, end_value):
    mid = (start + end) // 2
    mid_value = start_value - (mid - start)

    if mid == t:
        return mid_value

    elif mid > t:
        end = mid - 1
        return binaryCycle(t, start, end, start_value, mid_value + 1)

    elif mid < t:
        start = mid + 1
        return binaryCycle(t, start, end, mid_value - 1, end_value)


def cycle(t):
    i = 1
    j = 0
    m = 3
    count = 0

    while True:
        count += 1
        j = i + m
        if i <= t < j:
            break

        i = j
        m *= 2

    return i


t = 22
t = 17
t = 4

print(strangeCounter(t))