'''
Question: Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example:

Input:
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4

Output:
true

Explanation:
It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


So we will take our original array and try to form k buckets where:

Let "sum" be the sum of all elements in the array.

Each bucket has a sum of sum / k (aka we take the whole array's sum and have each bucket be an equal cut of that total cumulative sum...hence "K EQUAL SUM SUBSETS").


Validation

We can't do this if:

k is 0 or less.

sum % k is not 0 (meaning the total sum of the array does not allow us to have k equal sum buckets...we are only working with integers).


Code Explanation

The Driver Function:

We get the sum of the number to validate that we can have k equal sum buckets without having non-integer sums on each bucket
k also cannot be less than or equal to 0.

If all checks out we go into the recursion.

The Recursion:

Our approach here will be to fill each bucket with unique items, never placing an item in more than 1 bucket.

Each recursion frame will go through and try placing an item that has not been placed in a bucket (we keep track of placed items) and then we recurse with that item placed.

This is why we advance start by 1, we only use items past the item we just picked.

We also add the item's value to our working sum.

When we have filled a bucket, we will continue on with the recursion while keeping the used items marked as seen and we set the start to 0 since the whole array is eligible again as long as an item has not been used yet and we set the working sum to 0 since we are working on a new bucket.

WHEN WE FILL K - 1 BUCKETS, WE ARE DONE. This is because if we filled k - 1 buckets, the last bucket MUST be fillable since sum % k == 0.

Since we could fill all other buckets up to that point equally, we know for sure that we could finish the last bucket without things spilling over or going under value.


Complexities

Took me 3 hours of back and forth of thinking and I could still not pin the space complexity down to a point I could CLEARLY explain a given upper bound on time.

No one on Leetcode is sure and the moderators have very opaque explanations as always. I will leave this alone.

Time: O( ? )

Space: O( n )
Boolean array to mark used elements entails an automatic O(n) space.

Also, we will place nearly n items so the call stack will grow in a linear fashion with the input size but this is an after-consideration. The boolean array puts us at O(n) space at least from the beginning.

'''
from typing import List, Set
def canPartitionEqualSubsets(nums: List, k: int) -> bool:
    total_sum = sum(nums)
    if k == 0:
        return False
    if total_sum % k == 0:
        return canPartition(nums, 0, k, total_sum / k)

    return False

def canPartition(nums: List, current_sum: int, k: int, sub_total: int, cache: Set = set()) -> bool:
    if k == 1:
        return True

    if current_sum == sub_total:
        return canPartition(nums, 0, k - 1, 0)

    for num in nums:
        if num not in cache:
            cache.add(num)
            if canPartition(nums, current_sum + num, k, sub_total):
                return True
            cache.discard(num)

    return False


nums = [4, 3, 2, 3, 5, 2, 1]
k = 4

res = canPartitionEqualSubsets(nums, k)
print(res)