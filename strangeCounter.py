
def strangeCounter(t):
    i = cycle(t)
    value = i + 2

    while True:
        if i == t:
            break

        i += 1
        value -= 1

    return value

    # time, value = cycle(t)
    # end = time + value
    # t1 = time
    #
    # while t1 < end:
    #     if t == t1:
    #         break
    #
    #     t1 += 1
    #     value -= 1
    #
    # return value

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


# def strangeCounter(t):
#     start, end = cycle(t)
#     value = start + 2
#     t1 = start
#
#     while t1 <= end:
#         if t == t1:
#             break
#
#         t1 += 1
#         value -= 1
#
#     return value

# def cycle(t):
#     num = 1
#     factor = 3
#
#     while True:
#         if t in range(num, num+factor):
#             break
#
#         num += factor
#         factor *= 2
#
#     return num, factor

# def cycle(t):
#     t1 = 1
#     cycle = 0
#     start = 0
#     end = 0
#
#     while True:
#         v = t1 + 2
#         t2 = t1 + v
#         cycle += 1
#         if t1 <= t < t2:
#             start = t1
#             end = t2 - 1
#             break
#
#         t1 = t2
#     return start, end

# def cycle(t):
#     t1 = 1
#     cycle = 0
#     start = 0
#     end = 0
#
#     while True:
#         v = t1 + 2
#         t2 = t1 + v
#         cycle += 1
#         if t1 <= t < t2:
#             start = t1
#             end = t2 - 1
#             break
#
#         t1 = t2
#     return start, end

t = 4
# t = 5
# t = 9
# t = 10
# t = 21


t = 22
t = 17
t = 4

print(strangeCounter(t))