def jumpingOnClouds(c, k):
    # n = len(c)
    started = True
    energy = 100
    i = 0

    while i > 0 or started:
        started = False
        i = (i + k) % len(c)
        energy -= (1 + (c[i] == 1) * 2)

    return energy