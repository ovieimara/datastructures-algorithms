import random


def generateRandomArr(num):
    random_numbers = random.sample(range(-10, 11), num)
    print(random_numbers)
    return random_numbers

def convertStringToList(numbers):
    return list(map(int, numbers.split()))

def all_equal(lst):
    return all(x == lst[0] for x in lst)