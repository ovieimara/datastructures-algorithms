import string


def countFamilyLogins(logins):
    # Write your code here
    alphabet = list(string.ascii_lowercase)
    alphaDict = {c: i for i, c in enumerate(alphabet)}
    size = len(logins)
    result = []

    loginsFreq = getLoginsFreq(logins)

    for i in range(size):
        updated = False
        for j in range(size):
            a = logins[i]
            b = logins[j]

            if a == b:
                continue

            if loginsFreq[b] > 0 and compare(a, b, alphaDict):
                    result.append((a, b))
                    loginsFreq[b] -= 1
                    updated = True
                    print(a, loginsFreq)
        if updated:
            loginsFreq[a] -= 1

    print(result)
    return len(result)

def getLoginsFreq(logins):
    store = {}

    for i in range(len(logins)):
        login = logins[i]
        freq = store.get(login, 0)
        store[login] = freq + 1

    print(store)
    return store


def compare(a, b, alphaDict):

    for i in range(len(a)):
        char1 = a[i]
        char2 = b[i]
        idx1 = alphaDict.get(char1)
        idx2 = alphaDict.get(char2)
        id1 = (idx1 + 1) % 26
        id2 = (idx2 + 1) % 26

        if id1 != idx2 and idx1 != id2:
            return False

    return True

logins = ['bag', 'sfe', 'cbh', 'cbh', 'red']
# logins = ['corn', 'horn', 'dpso', 'eqtp', 'corn']
logins = ["ebu", "bat", "cbu", "ebu"]
val = countFamilyLogins(logins)
print(val)