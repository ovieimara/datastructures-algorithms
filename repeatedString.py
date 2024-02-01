#complexity: Time: O(m), space = O(1)

def repeatedString(s, n):
    # Write your code here
    m = len(s)
    store = [0] * 26

    for c in s:
        idx = ord(c) - ord('a')
        store[idx] += 1

    store[0] *= (n // m)
    for i in range(n % m):
        if s[i] == 'a':
            store[0] += 1

    return store[0]
