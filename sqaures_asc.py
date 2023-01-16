import math
import random


def squares_asc(arr):
    left = 0
    right = i = len(arr) - 1
    new_arr = [0 for x in arr]
    arr.sort()
    print(arr)

    while left <= right:
        a = math.pow(arr[left], 2)
        b =  math.pow(arr[right], 2)
        # new_arr[right] = max(a, b)
        if a > b:
            new_arr[i] = a
            left += 1
        else:
            new_arr[i] = b
            right -= 1

        i -= 1
    return  new_arr

def swap(l, r, arr):
    arr[l], arr[r] = arr[r], math.pow(arr[l], 2)

def generateRandomArr(num):
    random_numbers = random.sample(range(-10, 11), num)
    print(random_numbers)
    return random_numbers

def is_sorted(lst):
    return lst == sorted(lst)

arr = [-4, 1, 2, 3]
# arr = generateRandomArr(5)
res = squares_asc(arr)
print(res)
print(is_sorted(res))

