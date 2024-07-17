import string
from typing import List
import itertools


# Base class
class BaseProcessor:
    def __init__(self):
        pass
    # Method to remove punctuation from a string
    def remove_punctuation(self, input_string: str):
        result = []
        for c in input_string:
            if c.isalpha() or c.isspace():
                result.append(c)
            else:
                result.append(' ')

        return ''.join(result)

# Inherited class
class AdvancedProcessor(BaseProcessor):
    def __init__(self):
        ### Complete the initialisation of base class
        super().__init__()

    # Method to check if a number is prime
    def is_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Method to filter prime numbers from a list
    def filter_primes(self, num_list):
        ### Filter the list of prime numbers and return
        return [num for num in num_list if self.is_prime(num)]

def is_primes(arr: List):
    size = len(arr)
    result = [True] * size

    for i in range(0, size//2 + 1):
        if result[i]:
            j = i + arr[i]
            while j < size:
                result[j] = False
                j += arr[i]

    return [n for b, n in zip(result, arr) if b]

# Test remove_punctuation method
processor = AdvancedProcessor()
test_string = "Hello, World! This is a test-string."
print("Original String:", test_string)
print("Without Punctuation:", processor.remove_punctuation(test_string))

# Test filter_primes method
test_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Original List:", test_list)
print("Prime Numbers:", processor.filter_primes(test_list))

res = is_primes(test_list)
print(res)

