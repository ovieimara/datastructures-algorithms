def gcd(a, b):
    if b == 0:
        return a

    remainder = a % b
    return gcd(b, remainder)

res = gcd(357, 234)
print(res)