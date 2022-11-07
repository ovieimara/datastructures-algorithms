import math
def waiter(number, q):
    # Write your code here
    # print(number)
    if q == 0:
        return number[:: -1]

    if not number:
        return []

    primes = []
    multiplier = 1
    while len(primes) < len(number):
        primes = generatePrimes(len(number) * multiplier)
        multiplier += 2
    # print(primes)
    answers = []
    stackA = []

    for i in range(0, q):
        stackA = []
        stackB = []
        for j in range(len(number) - 1, -1, -1):
            num = number[j]
            if num % primes[i] == 0:
                stackB.append(num)
            else:
                stackA.append(num)

        number = stackA
        answers.extend(stackB[:: -1])

    answers.extend(number[:: -1])

    return answers


def generatePrimes(num):
    # print('Prime:', num)
    primes = [2, 3, 5, 7, 11, 13]
    for x in range(17, num + 1):
        if isPrime(x):
            print(f'{x} is a prime number')
            primes.append(x)
    print(primes)
    return primes


def isPrime(num):
    # print(num)
    for x in range(2, math.floor(math.sqrt(num)) + 1):
        if num % x == 0:
            # print(num, False)
            return False

    # print(num, True)
    return True
