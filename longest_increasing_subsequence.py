'''
Question: Given an array of all integers that may or may not be sorted, determine the length of the longest subsequence that is strictly non-decreasing.

What Is A Subsequence?

A subsequence of an array is a subset of the array that maintains temporal order.

It does not have to be contiguous but it might turn out to be contiguous by chance.


Problem Name / Variants

This problem also comes in the form of asking for the longest strictly decreasing subsequence.

This is longest non-decreasing subsequence meaning that we will have a non-strictly increasing subsequence (aka we can have deltas of 0 between contiguous elements in the subsequence).


Approach 1 (Brute Force)

We can enumerate all 2^n subsets of the original array and then test them for the non-decreasing property.

The answer will be the longest subset that has the property.

This is too expensive.


Approach 2 (Dynamic Programming)

Do you see the potential for a subproblem here?

If you do, then we have the opportunity to use dynamic programming.

Example
[ -1, 3, 4, 5, 2, 8 ]

At the index 0 I always know that I can have a subsequence of length 1.

In fact, at all positions the longest non-decreasing subsequence can be at least length 1.

We then look at index 1, I need to ask myself if the item at index 1 can lengthen the longest subseqence found at index 0.

We check if 3 is greater than or equal to 1...it is. Great. index 1 can be tacked on but...should I?

The LNDS (longest non-decreasing subsequence) at index 1 is 0.

The LNDS at index 0 is 1.

Yeah...it makes sense because if I tack 3 onto the LNDS I found for the subproblem of just [ -1 ] then at index 1 I will also have a LDNS.

So what we basically do is build a table and ask ourselves these questions all along the way.

EACH CELL REPRESENTS THE ANSWER TO THE SUBPROBLEM ASKED AGAINST the subsequence from index 0 to index i (including the element at index i).


Complexities:

Time: O( n^2 )

n is the length of the array.

For each of the n elements we will solve the LNDS problem which takes O(n) time, therefore we yield a O( n^2 ) runtime complexity.

Space: O( n )

We will store our answers for each of the n LNDS subproblems.
'''
from typing import List


def longest_increasing_subsequence(arr):
    subs = []
    # subsequence(arr, 0, 1, [arr[0]], subs)
    # return max(subs)
    return subsequence(arr)

#bottom to top
def subsequence(arr):
    size = len(arr)
    cache = [1] * size

    for i in range(1, size):
        for j in range(0, i):
            if arr[i] >= arr[j]:
                cache[i] = max(cache[i], cache[j] + 1)

    print(cache)
    return cache[-1]

#top to bottom
# def subsequence(arr: List, i: int, j: int, sub: List, subs: List):
#     if j >= len(arr):
#         subs.append(len(sub))
#         return
#
#     if arr[j] >= sub[-1]:
#         subsequence(arr, i, j+1, sub+[arr[j]], subs)
#
#     subsequence(arr, i, j+1, sub, subs)


arr = [-1, 3, 4, 5, 2, 8]
arr = [-1, 3, 4, 5, 2, 2, 2, 2]
res = longest_increasing_subsequence(arr)
print(res)

