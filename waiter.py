import math
from collections import deque
from typing import List


def waiter(number, q):
    number = number[::-1]
    answers = []
    odds = []
    prime_numbers = primes(q)
    arr = number[:]

    for i in range(q):
        if i > 0:
            arr = odds
        odds = []
        for num in arr[::-1]:
            if num % prime_numbers[i] == 0:
                answers.append(num)
            else:
                odds.append(num)

    answers.extend(odds)
    return answers

def primes(n: int) -> List:
    num = 17
    prime_numbers = [2, 3, 5, 7, 11, 13, 17]

    while len(prime_numbers) < n:
        num += 1
        is_prime = True
        for i in range(2, math.floor(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(num)

    return prime_numbers


# def waiter(number, q):
#     # Write your code here
#     # print(number)
#     if q == 0:
#         return number[:: -1]
#
#     if not number:
#         return []
#
#     primes = []
#     multiplier = 1
#     while len(primes) < len(number):
#         primes = generatePrimes(len(number) * multiplier)
#         multiplier += 2
#     # print(primes)
#     answers = []
#     stackA = []
#
#     for i in range(0, q):
#         stackA = []
#         stackB = []
#         for j in range(len(number) - 1, -1, -1):
#             num = number[j]
#             if num % primes[i] == 0:
#                 stackB.append(num)
#             else:
#                 stackA.append(num)
#
#         number = stackA
#         answers.extend(stackB[:: -1])
#
#     answers.extend(number[:: -1])
#
#     return answers
#
#
# def generatePrimes(num):
#     # print('Prime:', num)
#     primes = [2, 3, 5, 7, 11, 13]
#     for x in range(17, num + 1):
#         if isPrime(x):
#             print(f'{x} is a prime number')
#             primes.append(x)
#     print(primes)
#     return primes


# def isPrime(num):
#     # print(num)
#     for x in range(2, math.floor(math.sqrt(num)) + 1):
#         if num % x == 0:
#             # print(num, False)
#             return False
#
#     # print(num, True)
#     return True


# def primes(n: int) -> List:
#     primes_arr = [False] * (n+1)
#     primes_arr[0] = True
#     primes_arr[1] = True
#     p = []
#
#     for i in range(n+1):
#         if primes_arr[i]:
#             k = 1
#             val = i + 2
#             j = val * k
#             p.append(val)
#             while j < n+1:
#                 num = j + 2
#                 if num % 2 > 0:
#                     primes_arr[j] = True
#                 # print(j, num, primes_arr[j])
#
#                 k += 1
#                 j = val * k
#         i += 1
#
#     return p

#
# if __name__ == '__main_':
#     print('ovie')
number = [2, 3, 4, 5, 6, 7]
q = 3
number = [3, 4, 7, 6, 5]
q = 1
number = [3, 3, 4, 4, 9]
q = 2

number = [80, 37, 86, 79, 8, 39, 43, 41, 15, 33, 30, 15, 45, 55, 61, 74, 49, 49, 20, 66, 77, 19, 85, 44, 81, 82, 27, 5, 36, 83, 91, 45, 39, 44, 19, 44, 71, 49, 8, 66, 81, 40, 29, 60, 35, 31, 44]
q = 21

res = waiter(number, q)
print(res)