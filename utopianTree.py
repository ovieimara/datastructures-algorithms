import math

# def utopianTree(n):
#     # Write your code here
#     end = math.ceil(n / 2)
#     height = 0
#     for i in range(1, end + 1):
#         height += (2 ** i)
#
#     return height if n % 2 > 0 else height + 1


def utopianTree(n):
    return (2 * ((2 ** math.ceil(n/2)) - 1)) + (n % 2 == 0) * 1