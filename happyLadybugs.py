def happyLadybugs(b):
    memo = {}

    if len(b) == 1 and (65 <= ord(b) <= 90):
        return 'NO'
    elif len(b) == 1 and ord(b) == 95:
        return 'YES'

    if isHappy(b):
        return 'YES'

    bugs = []
    for bug in b:
        bugs.append(bug)
        count = memo.get(bug, 0)
        if 65 <= ord(bug) <= 90:
            memo[bug] = count + 1

    bugs.sort()

    if all(bugs[i] == bugs[i-1] for i in range(1, len(bugs))):
        return 'YES'

    if ord(bugs[-1]) == 95 and 1 not in memo.values():
        return 'YES'

    return 'NO'

def isHappy(bugs):
    i = 1
    prev = ''
    if bugs[0] != bugs[1]:
        return False

    if bugs[len(bugs) - 2] != bugs[len(bugs) - 1]:
        return False

    while i < len(bugs)-1:
        if (bugs[i] != bugs[i-1]) and (bugs[i] != bugs[i+1]):
            print(i)
            return False
        i += 1

    return True


# b = "RBY_YBR"
b = "YYR_B_BR"
b = "X_Y__X"
b = "__"
b = "B_RRBR"
b = "AABBC"
# b = "AABBC_C"
b = "_"
# b = "DD__FQ_QQF"
# b = "AABCBC"
# b = "AAAAAAA"
# b = "A"
# b = "RRGGBBXY"
# b = "RRGGBBXX"

print(happyLadybugs(b))