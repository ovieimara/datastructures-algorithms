def jumpingOnClouds(c):
    ''''''
    return jumpCloud(c, 0)


def jumpCloud(c, idx):
    # print(len(c), idx)
    if idx >= len(c) - 1:
        return 0
    if c[idx] == 1:
        return float('inf')

    return 1 + min(jumpCloud(c, idx + 1), jumpCloud(c, idx + 2))

c = [0, 1, 0, 0, 0, 1, 0]
c = [0, 0, 1, 0, 0, 1, 0]
c = [0, 0, 0, 0, 1, 0]
res = jumpingOnClouds(c)
print(res)