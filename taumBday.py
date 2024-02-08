
def taumBday(b, w, bc, wc, z):

    return (bc * b) + (bc + z) * w if wc > bc + z else (wc * w) + (wc + z) * b if bc > wc + z else (wc * w) + (bc * b)


# w = 10
# b = 10
# bc = 1
# wc = 1
# z = 1

b = 5
w = 9
bc = 2
wc = 3
z = 4

b = 3
w = 6
bc = 9
wc = 1
z = 1

b = 7
w = 7
bc = 4
wc = 2
z = 1

b = 3
w = 3
bc = 1
wc = 9
z = 2

print(taumBday(b, w, bc, wc, z))