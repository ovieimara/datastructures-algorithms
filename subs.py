import time
from typing import List


#substring/subarray
def subString(arr):
    size = len(arr)
    subStrings = []
    for l in range(1, size+1):
        for i in range(0, size-l+1):
            subs = arr[i: i+l]
            subStrings.append(subs)

    return subStrings

# arr = [1, 2, 3, 4]
# res = subString(arr)
# print(res)

def subsequence(arr):
    sub = []
    subs = []
    start = time.perf_counter()
    getSubsequence(arr, 0, sub, subs)
    finish = time.perf_counter()
    print((finish - start))
    return subs
def getSubsequence(arr, i, sub, subs: List, memcache={}):
    key = str(i) + '' + str(subs)
    if key in memcache:
        return
    if i == len(arr):
        subs.append(sub)
        return

    getSubsequence(arr, i+1, sub+[arr[i]], subs)
    getSubsequence(arr, i+1, sub, subs)

arr = [1, 2, 3, 4]
res = subsequence(arr)
print(res)

def countVowels(sub):
    count = 0
    for c in sub:
        if c in {'a', 'e', 'i', 'o', 'u'}:
            count += 1
    return count

def subStringWithVowelsWithK(s, k):
    size = len(s)
    count = countVowels(s[0: k])
    max_count = count
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for start in range(1, size-k+1):
        sub = s[start: start+k]
        removed = s[start-1]
        entered = s[start+k-1]
        if removed in vowels:
            count -= 1
        if entered in vowels:
            count += 1

        print(sub, removed, entered, count)

        max_count = max(max_count, count)

    return max_count

# s = 'myitemissexy'
# k = 14
# res = subStringWithVowelsWithK(s, k)
# print(res)

def subStringWithVowels(s):
    size = len(s)
    # count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_count = 0

    for l in range(1, size+1):
        count = countVowels(s[: l])
        max_count = max(max_count, count)

        for i in range(1, size-l):
            removed = s[i-1]
            entered = s[i+l-1]
            if removed in vowels:
                count -= 1
            if entered in vowels:
                count += 1

            max_count = max(max_count, count)

    return max_count

# s = 'myitemissexy'
# res = subStringWithVowels(s)
# print(res)


def subset(arr):
    size = len(arr)
    subs = [[]]

    for num in arr:
        for i in range(len(subs)):
            subs.append(subs[i]+[num])

    return subs

arr = [1, 2, 3, 4]
res = subset(arr)
print(res)

