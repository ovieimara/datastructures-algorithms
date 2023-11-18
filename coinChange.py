# def coinChange(amount, coins, change = 0):
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

def coinChange(amount, coins, change = 0):
    if amount < 0:
        return float("inf")
    if amount == 0:
        return change

    min_coins = float("inf")
    for coin in coins:
        # if amount - coin >= 0:
            # print(amount - coin)
            min_coins = min(min_coins, coinChange(amount - coin, coins, change + 1))
    return min_coins

amount = 15
coins = [2, 3, 7]
#
# amount = 10
# coins = [2, 5, 3, 6]

# amount = 4
# coins = [1, 2, 3]
#
# amount = 11
# coins = [9, 6, 5, 1]

# amount = 30
# coins = [25, 10, 5]

# amount = 13
# coins = [9, 6, 5, 1]

# amount = 18
# coins = [1, 3, 5, 7]

res = coinChange(amount, coins)
print(res)
