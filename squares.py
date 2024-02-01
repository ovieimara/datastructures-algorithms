import math


def squares(a, b):
    # Write your code here
    x = math.ceil(math.sqrt(a))
    y = math.floor(math.sqrt(b))

    return y - x + 1

def squares(a, b):
    x = math.ceil(math.sqrt(a))
    sqrs = 0
    while x * x <= b:
        sqrs += 1
        x += 1
    return sqrs