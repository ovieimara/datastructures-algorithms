

def howManyGames(p, d, m, s):

    curr_val = p
    total = 0
    count = 0
    while total + curr_val <= s:
        total += curr_val
        curr_val = max(curr_val - d, m)
        count += 1

    return count

p = 20
d = 3
m = 6
s = 85


p = 20
d = 3
m = 6
s = 80


p = 20
d = 3
m = 6
s = 70




print(howManyGames(p, d, m, s))