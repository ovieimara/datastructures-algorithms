from typing import List


def longest_common_substring(string1, string2):
    return lcs(string1, string2, 0, 0)


def lcs(string1: str, string2: str, i:int, j: int, count: int = 0):
    if i == len(string1) or j == len(string2):
        return count
    if string1[i] == string2[j]:
        return lcs(string1, string2, i+1, j+1, count+1)
    else:
        return max(lcs(string1, string2, i+1, j), lcs(string1, string2, i, j+1))

def longestCommonSubstringDynamic(string1: str, string2: str):
    m = len(string1)
    n = len(string2)
    arr = [[0] * (m) for _ in range(n)]

    for c in range(m):
        if string1[c] == string2[0]:
            arr[0][c] = 1
        else:
            arr[0][c] = 0

    for r in range(n):
        if string2[r] == string1[0]:
            arr[r][0] = 1

        else:
            arr[r][0] = 0

    longest = 0
    for i in range(1, n):
        for j in range(1, m):
            if string1[j] == string2[i]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = 0

            longest = max(longest, arr[i][j])

    return longest


def longest_common_substings(string1, string2):
    subs = [[]]
    lcsubstrings(string1, string2, 0, 0, [], subs)
    return subs


def lcsubstrings(string1: str, string2: str, i: int, j: int, sub: List, subs: List):
    if i == len(string1) or j == len(string2) and len(sub) > len(subs[-1]):
        subs[-1] = sub
        return

    if string1[i] == string2[j]:
        lcsubstrings(string1, string2, i+1, j+1, sub + [string1[i]], subs)
    else:
        lcsubstrings(string1, string2, i+1, j, sub, subs)
        lcsubstrings(string1, string2, i, j+1, sub, subs)


def longestCommonSubsequenceDynamic(string1: str, string2: str):
    m = len(string1)
    n = len(string2)
    arr = [[0] * (m+1) for _ in range(n+1)]
    arr[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string2[i-1] == string1[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i][j-1], arr[i-1][j])
    # print(arr)
    return arr[-1][-1]


def longest_common_substing_multiple(strings: List):
    return lcs_multiple(strings)


def lcs_multiple(strings: List):
    min_string = min(strings, key=len)
    size = len(min_string)

    results = ''
    for l in range(1, size+1):
        for start in range(0, size-l+1):
            sub = min_string[start: start+l]
            print(sub)

            if all(sub in string for string in strings) and len(sub) > len(results):
                results = sub

    return results




string1 = 'flower'
string2 = 'flow'
string3 = "flaunt"
string4 = "aunt"
res = longest_common_substring(string1, string2)
res2 = longestCommonSubstringDynamic(string1, string2)
strings = ['flower', 'flow', "flaunt"]
res3 = longest_common_substings(string4, string3)
res4 = longest_common_substing_multiple(strings)
print(res)
print(res2)
print(res3)
print(res4)



