

def biggerIsGreater(w):

    n = len(w)

    i = n - 2

    while i >= 0 and w[i] >= w[i+1]:
        i-= 1

    if i < 0:
        return 'no answer'

    j = n - 1
    while j >= 0 and w[j] <= w[i]:
        j -= 1

    new_w = w[ : i] + w[j] + w[i + 1 : j] + w[i] + w[j + 1: ]

    return new_w[: i+1] + new_w[ : i : -1]

# w = "abcd"
# w = "ab"
# w = "bb"
# w = "hefg"
# w = "dhck"
# w = "dkhc"
# w = "lmno"
# w = "dcba"
# w = "dcbb"
# w = "abdc"
# w = "fedcbabcd"
# w = "aabb"
# w = "abab"
# w = "a"
# w = "bb"
w = "dacbb"
w = "fghca"
print(biggerIsGreater(w))
