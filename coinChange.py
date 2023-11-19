#Recursion 1
#complexity: Time: O(m ** n), space = O(n) where n = amount, m = len(coins)
# def minCoinChange(amount, coins, change = 0):
#     if amount < 0:
#         return float("inf")
#     if amount == 0:
#         return 0
#
#     min_coins = float("inf")
#     for coin in coins:
#         # if amount - coin >= 0:
#             # print(amount - coin)
#             min_coins = min(min_coins, 1 + coinChange(amount - coin, coins))
#     return min_coins

#Recursion 2
#complexity: Time: O(m ** n), space = O(n) where n = amount, m = len(coins)
# def minCoinChange(amount, coins, change = 0):
#     if amount < 0:
#         return float("inf")
#     if amount == 0:
#         return change
#
#     min_coins = float("inf")
#     for coin in coins:
#         # if amount - coin >= 0:
#             # print(amount - coin)
#             min_coins = min(min_coins, coinChange(amount - coin, coins, change + 1))
#     return min_coins

#dynamic programming
#complexity: Time: O(n x m), space = O(n) where n = amount, m = len(coins)
def minCoinChange(amount, coins):
    min_coin_arr = [float("inf")] * (amount + 1)
    min_coin_arr[0] = 0

    min_coins = float("inf")

    for i in range(1, amount + 1):
        min_coin_arr[0] = 0
        # min_coins = float("inf")
        for j in range(1, len(coins)):
            if i - coins[j-1] >= 0:
                min_coin_arr[i] = min(min_coins, min_coin_arr[i - coins[j-1]] + 1)

    return min_coin_arr[-1]




amount = 15
coins = [2, 3, 7]
#
# amount = 10
# coins = [2, 5, 3, 6]

amount = 4
coins = [1, 2, 3]
#
# amount = 11
# coins = [9, 6, 5, 1]

# amount = 30
# coins = [25, 10, 5]

# amount = 13
# coins = [9, 6, 5, 1]

# amount = 18
# coins = [1, 3, 5, 7]

res = minCoinChange(amount, coins)
print(res)

'''
Asumptions;

1. If u have to make change for zero amount, no of min coins need is zero

2. If u have zero coins and u need to make change for amount 1 2 3 4, u cant make any change, so we say it is undefined and give it the value float('inf') since we are looking for minimum

3. If amount - coin < 0 then minimum required coins is the value float('inf')
'''