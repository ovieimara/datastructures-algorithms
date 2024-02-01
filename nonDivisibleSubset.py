from input import input

def nonDivisibleSubset(k, s):
    rem_count = [0]*k
    for num in s:
        rem_count[num % k] += 1
        result = 0

    if rem_count[0] > 0:
        result += 1

    for i in range(1, k // 2 + 1):
        if i != k - i:
            result += max(rem_count[i], rem_count[k - i])
        else:
            result += 1

    return result
# def nonDivisibleSubset(k, s):
#
#     subsets = []
#     subs = []
#     idx = 0
#     # nonDivisibleSubsetRec(k, s, idx, subs, subsets)
#     # print(subsets)
#     # return len(findMaximalSubset(subsets, k)[0])
#     # results = nonDivisibleSubsetPointer(k, s)
#     # max_len = float('-inf')
#     # for res in results:
#     #     max_len = max(max_len, len(res))
#     return nonDivisibleSub(k, s)
#
#     # return max_len
#
#
# def nonDivisibleSub(k, s):
#     subsets = [[]]
#
#     for i in range(0, len(s)):
#         subs = []
#         for sub in subsets:
#             take = sub + [s[i]]
#             leave = sub
#             subs.append(take)
#             subs.append(leave)
#         subsets = subs
#
#     return findMaxima(subsets, k)
#     # print(subsets)
#
#
# def findMaxima(subsets, k):
#     result = [[]]
#
#     for subset in subsets:
#         is_maxi = True
#         for i in range(len(subset) - 1):
#             for j in range(i + 1, len(subset)):
#                 # print(subset[i], subset[j], subset)
#                 if (subset[i] + subset[j]) % k == 0:
#                     is_maxi = False
#                     # break
#         # print(is_maxi)
#         if is_maxi and len(result[-1]) < len(subset):
#             result[-1] = subset
#
#     # print(result)
#
#     return len(result[-1])
#
# def nonDivisibleSubsetPointer(k, s):
#     i = 0
#     j = len(s) - 1
#     s.sort()
#     print(s)
#     subset = set()
#     result = []
#
#     while i < j:
#         print(s[i], s[j])
#         if (s[i] + s[j]) % k > 0:
#             subset.add(s[i])
#             subset.add(s[j])
#             j -= 1
#         else:
#             subs = list(subset)[:]
#             result.append(subs)
#             subset.clear()
#             i += 1
#
#     if len(subset) > 0:
#         result.append(subset)
#     return result
# def nonDivisibleSubsetRec(k, s, idx, subs, subsets):
#     if idx >= len(s):
#         subsets.append(subs)
#         return
#
#     nonDivisibleSubsetRec(k, s, idx + 1, subs + [s[idx]], subsets)
#     nonDivisibleSubsetRec(k, s, idx + 1, subs, subsets)
#
# def findMaximalSubset(subsets, k):
#     result = [[]]
#     # max_len = float('-inf')
#     for sub in subsets:
#         is_optimal = checkIfMaximal(sub, k)
#         if is_optimal:
#             if len(sub) > len(result[-1]):
#                 result[-1] = sub
#             result.append(sub)
#
#     return result
#
# # def checkIfMaximal(subset, k):
# #     for i in range(1, len(subset)):
# #         if (subset[i] + subset[i-1]) % k == 0:
# #             return False
# #
# #     return True
#
# def checkIfMaximal(subset, k):
#     res = True
#     for i in range(len(subset)):
#         for j in range(i+1, len(subset)):
#             if (subset[i] + subset[j]) % k == 0:
#                 res = False
#
#     return res

s = [1, 7, 2, 4]
k = 3

# s = [19, 10, 12, 24, 25, 22]
# k = 4
""
s = input.split()
k = 100

# s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
# k = 7
res = nonDivisibleSubset(k, s)
print(res)