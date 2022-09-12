'''
To build a house, the construction team levels a squared plot of land. You are given an array ground where ground[i] is a square i  height in meters.

Per one operation constructors lower or raise the square i by one meter. Determine the minimum number of operations to completely level the entire land plot.

Input:

ground  - integer array, 0<length(ground)<20, 0<ground[i]<200
Output:

Integer - number of operations to completely level the entire land plot, that is to make an entire array consist of the same values.
'''
import math

'''
Elon Musk presented a new space project - he launched a large number of rockets into the sky. There is an array rocket_pos, where rocket_pos[i] - the height of  i-th rocket and  rocket_speed array, where rocket_speed[i] - the speed of i-th rocket (the value of movement per time unit).

When the rockets reach the same height at some step, they unite into one rocket and their speed adds up.

Determine how many rockets will remain in the end.
'''
# def getChange(ground):
#     grounds = sorted(ground)
#     print(grounds)
#     count = 0
#     i = 0
#     j = len(grounds) - 1
#
#     while i < j:
#         first = grounds[i]
#         second = grounds[j]
#
#         if abs(second - first) == 1:
#             count += 1
#             #i += 1
#             grounds[i] = grounds[i] + 1
#             j -= 1
#
#         elif abs(second - first) == 2:
#             count += 2
#             grounds[i] = grounds[i] + 1
#             grounds[j] = grounds[j] - 1
#             i += 1
#             j -= 1
#
#         elif abs(second - first) == 0:
#             i += 1
#             j -= 1
#
#     print(count)
#     return count

#
# def getChange(ground):
#     size = len(ground)
#     grounds = ground[:]
#
#     count = 0
#
#     for i in range(1, size):
#         current = grounds[i]
#         prev = grounds[i - 1]
#
#         print((current - prev))
#         if (current - prev) == 2:
#             grounds[i - 1] = grounds[i - 1] + 1
#             count += 1
#
#         elif (current - prev) < 0:
#             grounds[i] = grounds[i] - 1
#             count += 1
#
#     print(count)
#     return count



# def getChange(ground):
#     items = {}
#     count = 0
#     max_val = 0
#     for i in ground:
#         val = items.get(i, 0)
#         val_count = val + 1
#         items[i] = val_count
#
#         if val_count > count:
#             max_val = i
#             count = val_count
#
#     print(max_val)
#
#     counter = 0
#     for x, i in enumerate(ground):
#         if i > max_val:
#             val = i - 1
#             ground[x] = val
#             if val == max_val:
#                 counter += 1
#
#         elif i < max_val:
#             val = i + 1
#             ground[x] = val
#             if val == max_val:
#                 counter += 1
#
#
#     print(ground, counter)
#     return counter


# def getChange(ground):
#     grounds = sorted(ground)
#     print(grounds)
#     count = 0
#     i = 0
#     j = len(grounds) - 1
#
#     while i < j:
#         first = grounds[i]
#         second = grounds[j]
#
#         if abs(second - first) == 1:
#
#             #i += 1
#             grounds[i] = grounds[i] + 1
#             j -= 1
#             if grounds[i] == grounds[j]
#                 count += 1
#
#         elif abs(second - first) > 1:
#             count += 2
#             grounds[i] = grounds[i] + 1
#             grounds[j] = grounds[j] - 1
#             i += 1
#             j -= 1
#
#         elif abs(second - first) == 0:
#             i += 1
#             j -= 1
#
#     print(count)
#     return count

# def getChange(ground):
#     grounds = sorted(ground)
#     cuts = [0] * len(grounds)
#     cuts[0] = 0
#     for i in range(1, len(grounds)):
#         cuts[i] = grounds[i] - grounds[i - 1] + cuts[i - 1]
#
#     return cuts[-1]

# def getChange(ground):
#     if len(ground) == 0:
#         return 0
#     grounds = sorted(ground)
#     cuts = grounds[:]
#     cuts[0] = 0
#     for i in range(1, len(grounds)):
#         cuts[i] = min(grounds[i] - grounds[i - 1] + cuts[i - 1], cuts[i])
#
#     print(cuts)
#     return cuts[-1]

# def getChange(ground):
#     if len(ground) == 0:
#         return 0
#
#     cuts = [0] * len(ground)
#     cuts[0] = 0
#
#     for i in range(1, len(ground)):
#         curr = ground[i]
#         prev = ground[i - 1]
#         if curr > prev:
#             diff = curr - prev
#             cuts[i] = cuts[i-1] + diff - 1
#
#         else:
#             diff = curr - prev
#             cuts[i] = cuts[i-1] + diff + 1
#
#     print(cuts)
#     return cuts[-1]

# def getChange(ground):
#     size = len(ground)
#     smallest = float('inf')
#     table = [[0 for _ in range(size)] for _ in range(size)]
#     for i in range(0, size):
#         if ground[0] == ground[i]:
#             table[i][0] = 0
#         else:
#             table[i][0] = 1
#
#
#     for row in range(0, 4):
#         for col in range(1, size):
#             if ground[row] == ground[col]:
#                 table[row][col] = table[row][col - 1] + 0
#             else:
#                 table[row][col] = table[row][col - 1] + 1
#
#         smallest = min(table[row][size - 1], smallest)
#         print(table)
#
#     return smallest

# def getChange(ground):
#     size = len(ground)
#     smallest = float('inf')
#     table = [[0 for _ in range(size)] for _ in range(size)]
#     for i in range(0, size):
#         table[i][0] = abs(ground[0] - ground[i])
#
#     print(table)
#
#     for row in range(0, size):
#         for col in range(1, size):
#             table[row][col] = table[row][col - 1] + abs(ground[row] - ground[col])
#
#         smallest = min(table[row][size - 1], smallest)
#
#     print(smallest)
#     return smallest
# k = getChange([1, 2, 2, 2])

# def get_result(ground):
#     size = len(ground)
#     table = [0] * size
#     miniOps = float("inf")
#     memCache = {}
#
#     for row in range(0, size):
#         rowTotal = 0
#         for col in range(0, size):
#             table[col] = addV(ground[row], ground[col], memCache)
#             rowTotal += table[col]
#
#         miniOps = min(rowTotal, miniOps)
#
#     return miniOps
#
#
# def addV(a, b, memCache):
#     val = memCache.get((a, b))
#     if val:
#         return val
#
#     c = abs(a - b)
#     memCache[(a, b)] = c
#     return c

# def get_result(ground):
#     size = len(ground)
#     table = [0] * size
#     miniOps = float("inf")
#     memCache = {}
#
#     for row in range(0, size):
#         table[0] = abs(ground[row] - ground[0])
#         for col in range(1, size):
#             table[col] = table[col - 1] + addV(ground[row], ground[col], memCache)
#
#         miniOps = min(table[-1], miniOps)
#
#     return miniOps


# def get_result(rocket_pos, rocket_speed):
#
#     step = 1
#     size = len(rocket_pos)
#     end = size
#     height = 0
#     # print(size)
#     while height <= 1000:
#         counter = {}
#
#         for i in range(size):
#             # if rocket_speed[i] <= 0:
#             #     height = 1005
#             #     break
#
#             if rocket_speed[i] > 0 and rocket_pos[i] > 0:
#                 height = (step * rocket_speed[i]) + rocket_pos[i]
#                 val = counter.get(height, 0)
#                 counter[height] = val + 1
#
#         end = min(end, len(counter))
#         step += 1
#         if end == 1:
#             break
#
#         # print(end)
#
#     return end

# k = get_result([], [])
#k = get_result([0, 0], [0, 0])
# k = get_result([2, 3], [1, 2])

# def get_result(rocket_pos, rocket_speed):
#     # Write your code here...
#     step = 1
#     size = len(rocket_pos)
#     end = size
#
#     while step <= 1000:
#         counter = {}
#
#         for position, speed in zip(rocket_pos, rocket_speed):
#
#             height = (step * speed) + position
#             val = counter.get(height, 0)
#             counter[height] = val + 1
#
#         end = min(end, len(counter))
#         step += 1
#         if end == 1:
#             break;
#
#     return end


# def maxSumIncreasingSubsequence(array):
#     # Write your code here.
#     sequences = [None] * len(array)
#     sums = array[:]
#     maxSumIdx = 0
#
#     for i in range(len(array)):
#         currentNum = array[i]
#         prevNum = 0
#
#         for i in range(len(array)):
#             currentNum = array[i]
#
#             for j in range(0, i):
#                 otherNum = array[j]
#                 prevNum = array[j - 1] if j > 0 else 0
#                 if otherNum > prevNum and otherNum < currentNum:
#                     sums[i] = max(sums[i], sums[j] + currentNum)
#                     sequences[i] = j
#
#         # for j in range(0, i):
#         #
#         #     otherNum = array[j]
#         #     if otherNum > prevNum and otherNum < currentNum:
#         #         sums[i] = max(sums[i], sums[j] + currentNum)
#         #         sequences[i] = j
#         #
#         #     prevNum = otherNum
#         #
#         if sums[i] > sums[maxSumIdx]:
#             maxSumIdx = i
#
#     print(sums)
#     return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]
#
#
# def buildSequence(array, sequences, maxSumIdx):
#     # print(sequences)
#     sequence = []
#     while maxSumIdx is not None:
#         sequence.append(array[maxSumIdx])
#         maxSumIdx = sequences[maxSumIdx]
#
#     return list(reversed(sequence))
#
# array = [8, 12, 2, 3, 15 , 5, 7]
# k = maxSumIncreasingSubsequence(array)

# def nonConstructibleChange(coins):
#     totalCoins = sum(coins)
#     size = len(coins)
#     count = 0
#
#     table = [[True for _ in range(totalCoins + 1)] for _ in range(size + 1)]
#
#     for i in range(1, totalCoins + 1):
#         table[0][i] = False
#
#     # print(table)
#
#     for i in range(1, size+1):
#         coin = coins[i-1]
#         for j in range(1, totalCoins + 1):
#             if j - coin >= 0:
#                 table[i][j] = table[i - 1][j - coin]
#             else:
#                 table[i][j] = table[i-1][j]
#
#             if i == size and table[i][j] == False:
#                 print(table)
#                 count = j
#                 break
#                 # return j-1
#     print(table)
#
#     return count
#
#
# coins = [1, 2, 5]
# coins = [5, 7, 1, 1, 2, 3, 22]
# k = nonConstructibleChange(coins)
# print(k)


# def closestNumbers(numbers):
#     # Write your code here
#     size = len(numbers)
#     minVal = float('inf')
#     table = [[float('inf') for _ in range(size)] for _ in range(size)]
#     exists = {}
#
#     for i in range(size):
#         for j in range(size):
#             if j != i:
#                 val = abs(numbers[i] - numbers[j])
#                 if val < minVal:
#                     minVal = val
#
#                 table[i][j] = val
#
#     for i in range(size):
#         for j in range(size):
#             if table[i][j] == minVal:
#                 key = str(min(numbers[i], numbers[j])) + str(max(numbers[i], numbers[j]))
#                 # print(key)
#                 exist = exists.get(key, False)
#                 if not exist:
#                     # pairs.append([min(numbers[i], numbers[j]), max(numbers[i], numbers[j])])
#                     print(min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))
#                     exists[key] = True

# Time = O(nlogn), space = O(1)
# def closestNumbers(numbers):
#     numbers.sort()
#     minVal = numbers[1] - numbers[0]
#
#     for i in range(1, len(numbers)):
#         val = numbers[i] - numbers[i-1]
#         if val == minVal:
#             print(numbers[i-1], numbers[i])

# def PalindromeChecker(s, startIndex, endIndex, subs):
#     size = len(startIndex)
#     length = len(s)
#     result = []
#
#     for i in range(size):
#         start = startIndex[i]
#         end = endIndex[i]
#         sub = subs[i]
#         subString = s[start:end+1]
#         subLength = len(subString)
#         rep = getSubs(subString)
#
#         #print('sub:', sub, rep)
#         if (subLength < length and rep <= sub) or (subLength == length and rep + 1 <= sub):
#             result.append('1')
#
#         else:
#             result.append('0')
#
#     return ''.join(result)
#
#
#
#
# def getSubs(s):
#     size = len(s)
#     midIdx = size // 2
#     left = []
#     right = []
#     #print(s)
#     store = storeInDict(s, size)
#
#     for i in range(midIdx, -1, -1):
#         #print(i)
#         val = s[i]
#         if store.get(val, 0) == 1:
#             left.append(val)
#
#     for i in range(midIdx + 1, size):
#         val = s[i]
#         if store.get(val, 0) == 1:
#             right.append(val)
#
#     l = len(left)
#     r = len(right)
#
#
#     rep = 0
#     if l > 0 and r > 0:
#         rep = min(l, r)
#     elif l > 0 and r == 0:
#         rep = l if l > 1 else 0
#     elif r > 0 and l == 0:
#         rep = r if r > 1 else 0
#
#
#     return rep
#
#
#
# def storeInDict(string, size):
#     store = {}
#     for i in range(size):
#         val = string[i]
#         count = store.get(val, 0)
#         store[val] = count + 1
#
#     return store
#
# #numbers = [6, 2, 4, 10]
# numbers = [4, 2, 1, 3]
# #print(closestNumbers(numbers))
# #s='xxanssugevu'
#
# # s ='cdecd'
# # startIndex = [0, 0, 0, 0]
# # endIndex = [0, 1, 2, 31]
# # subs = [0, 1, 1, 0]
# #
# # s = 'xxanssugevu'
# # startIndex = [0]
# # endIndex = [10]
# # subs = [31]
#
# s = "bcba"
# startIndex = [1, 2, 1]
# endIndex = [3, 3, 1]
# subs = [2, 0, 0]
#
# result = PalindromeChecker(s, startIndex, endIndex, subs)
# print(result)

# def movingMedian(arr):
#     n = arr[0]
#     newArray = arr[1:]
#     size = len(newArray)
#     output = [0] * size
#     subArray = []
#     for i in range(size):
#
#         if i < n:
#             subArray = newArray[0: i + 1]
#             sortArray = sorted(subArray)
#             print(subArray, sortArray)
#
#         else:
#             start = i - (n -1)
#             subArray = newArray[start: i + 1]
#             sortArray = sorted(subArray)
#             print(subArray, sortArray)
#
#         length = len(sortArray)
#         val = length // 2
#         if length == 2:
#             med = sum(sortArray) // 2
#         else:
#             med = sortArray[val]
#
#         output[i] = med
#
#     #print(output)
#     return output
#
# arr = [5, 2, 4, 6]
# arr = [3, 0, 0,-2, 0, 2, 0, -2]
# arr = [3, 1, 3, 5, 10, 6, 4, 3, 1]
# #arr = [1, 1, 3, 3, 3, 4, 5, 6, 10]
#
# med = movingMedian(arr)
# print(med)


# def decorator(orig_func):
#     def wrapper(*args):
#         print('before: ', orig_func(*args))
#         # reversed_args = args[-1::-1]
#         reversed_args = [args[i] for i in range(len(args)-1, -1, -1)]
#         print('after:', orig_func(*reversed_args))
#         return orig_func(*reversed_args)
#     return wrapper
#
# @decorator
# def maximum(a, b):
#     return a ** b
#
# print(maximum(2, 3))

'''
A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
def pangrams(s):
    # Write your code here
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    result = 'not pangram'
    alphabets = set()
    for x in s:
        if x.upper() in alpha:
            alphabets.add(x.upper())
    
    print(alphabets, len(alphabets))
    # if len(alphabets) >= 26:
    #     result = 'pangram'
    
    for x in alpha:
        if x not in alphabets:
            return 'not pangram'
        
        
    return 'pangram'
'''

def miniMaxSum(arr):
    '''
    Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four
     of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated
    long integers.
    Example
    arr = [1 2 3 4 5], [7 69 2 221 8974]
    The minimum sum is  and the maximum sum is . The function prints
    :param arr:
    :return:
    '''
    # Write your code here
    # size = len(arr)
    # table = [0] * size
    # minVal = float('inf')
    # maxVal = float('-inf')

    # for i in range(0, size):
    #     if i > 0:
    #         table[0] = arr[0]
    #     for j in range(1, size):
    #         table[j] = table[j-1] + arr[j] if j != i else table[j-1]

    #     if table[-1] > maxVal:
    #         maxVal = table[-1]

    #     if table[-1] < minVal:
    #         minVal = table[-1]

#     minVal = 0
#     maxVal = 0
#     arr.sort()
#
#     for i in range(0, len(arr) - 1):
#         minVal += arr[i]
#
#     for i in range(1, len(arr)):
#         maxVal += arr[i]
#
#     print(f'{minVal} {maxVal}')
#
#
# def timeConversion(s):
#     # Write your code here
#     hrs, mins, secs = s.split(':')
#     a = secs[2]
#     if a == 'P' and (12 > int(hrs) > 0):
#         hrs = int(hrs) + 12
#
#     if a == 'A' and int(hrs) == 12:
#         hrs = '00'
#
#     return f'{hrs}:{mins}:{secs[0:2]}'


# def flippingBits(n):
#     # Write your code here
#     binary = [0] * 32
#     size = len(binary)
#     sums = 0
#     idx = size - 1
#     q = n
#     p = 0
#
#     for i in range(size - 1, -1, -1):
#         if q > 0:
#             binary[i] = (q % 2) ^ 1
#             q = q // 2
#         else:
#             binary[i] = binary[i] ^ 1
#
#         sums = sums + (binary[i] * (2 ** p))
#         p += 1
#
#     return sums
#
# val = flippingBits(4)
# print(val)

# def birthday(s, d, m):
#     # Write your code here
#     table = []
#     size = len(s)
#     segment = 0
#
#     string = ''
#
#     store = {}
#
#     for i in range(size):
#         val = 0
#         for j in range(i, i + m):
#             if j < size:
#                 val += s[j]
#                 string += str(s[j])
#
#         if val == d:
#             store[string] = True
#
#     return len(store)
#
#
# def strings_xor(s, t):
#     res = ""
#     for i in range(len(s)):
#         if s[i] == t[i]:
#             res += '0';
#         else:
#             res += '1';
#
#     return res
#
# s = input()
# t = input()
# print(strings_xor(s, t))

#4294967291



# def fillQueues(left, right, queries, operations, stack, group):
#     inner_nodes = {'AND', 'OR', 'NOT', "CONTAINS", "IS"}
#     operation_nodes = {"CONTAINS", 'IS'}
#     group_nodes = {"AND", "OR"}
#
#     if left and left in inner_nodes:
#         if left in group_nodes:
#             group.append(left)
#         else:
#             # operations.append(left)
#             applyNotOperation(operations, left)
#
#     if right:
#         stack.append(right)
#         if left in operation_nodes:
#             queries.append(right)
#
#
# def getKeys(root):
#     left, right = None, None
#     item = [None, None]
#     if type(root) == dict:
#         for k, v in root.items():
#             item[0] = k
#             item[1] = v
#             # print('items: ', item)
#
#     return item
#
# def findLeaf(root):
#     stack = [root]
#     operations = []
#     queries = []
#     group = []
#
#     while stack:
#         node = stack.pop()
#         # print(node, type(node))
#         if type(node) == list:
#             for n in node:
#                 # print('node: ', n)
#                 left, right = getKeys(n)
#                 fillQueues(left, right, queries, operations, stack, group)
#         else:
#
#             left, right = getKeys(node)
#             fillQueues(left, right, queries, operations, stack, group)
#
#     # print(queries)
#     # print(applyNotOperation(operations))
#     # print(group)
#
#     s = createStatement(operations, group, queries)
#     print(s)
#     return operations
#
# def applyNotOperation(operations_node, node):
#     operations = {"CONTAINS", 'IS'}
#     neg = 'NOT'
#     #[[None, None], [None, 'IS'], [None, 'CONTAINS'], [None, 'NOT'], ['NOT, 'IS'], []]
#     print(operations_node, node)
#     if not operations_node:
#         operations_node.append([None, node])
#         return
#
#     if node in operations:
#         if operations_node[-1][0] is None and operations_node[-1][1] == neg:
#             operations_node[-1][0] = neg
#             operations_node[-1][1] = node
#
#         else:
#             operations_node.append([None, node])
#
#     else:
#         operations_node.append([None, neg])
#
#     # return operations_node
#
# def createStatement(operations_node, group_node, query):
#     statement = "SELECT * FROM LOG WHERE"
#     other = ""
#     val = ''
#     for i in range(len(query)):
#         # print(query[i])
#         # for k, v in query[i].items():
#         # print(list(query[i].items()))
#         k, v = list(query[i].items())[0]
#
#         val = 'NOT ILIKE' if operations_node[i][0] == 'NOT' else 'ILIKE'
#
#         other += f" {k} {val} '{'%%' if operations_node[i][1] == 'CONTAINS' else ''}{v}{'%%' if operations_node[i][1] == 'CONTAINS' else ''}' {group_node[i] if i < len(group_node) else ''}"
#
#     return statement + other

'''
{"NOT": {"OR": [{"AND": [{"IS": {"browser": "safari"}},{"IS": {"country": "Germany"}}]},{"CONTAINS": {"message": "stacktrace"}}]}}
'''



# t = {"CONTAINS":{"message": "error"}}
# t = {"IS":{"browser": "chrome"}}
# t = {"NOT": {"OR": [{"AND": [{"IS": {"browser": "safari"}},{"IS": {"country": "Germany"}}]},{"CONTAINS": {"message": "stacktrace"}}]}}

# val = findLeaf(t)
#
# print(val)

# l = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
#
# def get(str1, k):
#     s = len(l)
#     x = l.index(str1)
#     a = k%s
#     print(x+a)
#     return l[x+a]
#
# x = get('Mar', 1201)
#
# print(x)

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

#O(n2) time, O(1) space
# def flippingMatrix(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     sums = 0
#
#     for i in range(rows):
#         for j in range(cols):
#             matrix[i][j] = max(matrix[i][j], matrix[i][cols - 1 - j])
#
#
#     for i in range(rows):
#         for j in range(cols // 2):
#             matrix[i][j] = max(matrix[i][j], matrix[rows - 1 - i][j])
#
#
#     for i in range(rows//2):
#         for j in range(cols//2):
#             sums += matrix[i][j]
#
#     return sums
#
#
#
#
#
#
# matrix = [[112, 42, 83, 119],
#          [56, 125, 56, 49],
#          [15, 78, 101, 43],
#          [62, 98, 114, 108]]
#
# # matrix = [[1, 2], [3, 4]]
#
#  # matrix = \
#  #    [[107, 54, 128, 15],
#  #    [12, 75, 110, 138],
#  #    [100, 96, 34, 85],
#  #    [75, 15, 28, 112]]
# #488
# # val = flippingMatrix(matrix)
# # print(val)
#
# def findMedian(arr):
#     arr.sort()
#     size = len(arr)
#     midIdx = size // 2
#
#     return arr[midIdx]
#
# arr = [5,3,1,2,4]
# val = findMedian(arr)
# print(val)
#
#
# '''
# Given an array of n distinct integers, transform the array into a zig zag sequence by
# permuting the array elements. A sequence will be called a zig zag sequence if the
# first & elements in the sequence are in increasing order and the last k elements are
# in decreasing order, where k = (n + 1) /2. You need to find the lexicographically
# smallest zig zag sequence of the given array.
# Example
# a=[2, 3, 5, 1, 4]
# b = [1, 2, 3, 4, 5, 6, 7]
# Now if we permute the array as (1, 4, 5, 3, 2], the result is a zig zag sequence.
# '''
#
# def findZigZagSequence(a, n):
#     a.sort()
#     mid = int((n)/2)
#     a[mid], a[n-1] = a[n-1], a[mid]
#
#     st = mid + 1
#     ed = n - 2
#     while(st <= ed):
#         a[st], a[ed] = a[ed], a[st]
#         st = st + 1
#         ed = ed - 1
#
#     for i in range (n):
#         if i == n-1:
#             print(a[i])
#         else:
#             print(a[i], end = ' ')
#     return
#
#
# '''
# A teacher asks the class to open their books to a page number. A student can either
# start turning pages from the front of the book or from the back of the book. They
# always turn pages one at a time. When they open the book, page 1 is always on the
# right side:
# When they flip page 1, they see pages 2 and 3. Each page except the last page will
# always be printed on both sides. The last page may only be printed on the front,
# given the length of the book. If the book is n pages long, and a student wants to
# turn to page p, what is the minimum number of pages to turn? They can start at the
# beginning or the end of the book.
# Given n and p, find and print the minimum number of pages that must be turned in
# order to arrive at page p.
# Example
# n =5
# p=3
#
# n = 6
# p = 2
# '''
#
# def pageCount(n, p):
#     # Write your code here
#     left = 0
#     right = n if n % 2 > 0 else n + 1
#     num = 0
#
#     while left <= right:
#         x_left = left * 2
#         y_left = x_left + 1
#
#         y_right = right
#         x_right = y_right - 1
#
#         if x_left == p or y_left == p:
#             print(left)
#             return left
#
#         if y_right == p or x_right == p:
#             print(left)
#             return left
#
#         left += 1
#         right -= 2
#
#     return left
#
# '''
# Two players are playing a game of Tower Breakers! Player 1 always moves first, and
# both players always play optimally.The rules of the game are as follows:
# • Initiallv there are n towers.
# • Each tower is of height m.
# The players move in alternating turns.
# • In each turn, a player can choose a tower of height a and reduce its height to y,
# where 1 < y < a and y evenly divides a
# If the current player is unable to make a move, they lose the game.
# Given the values of n and m, determine which player will win. If the first player
# wins, return 1. Otherwise, return 2
# Example. n= 2
# m=6
# There are 2 towers, each 6 units tall. Player 1 has a choice of two moves:
# - remove 3 pieces from a tower to leave 3 as 6 modulo 3 = 0
# - remove 5 pieces to leave 1
# Let Plaver 1 remove 3. Now the towers are 3 and 6 units tall.
# Player 2 matches the move. Now the towers are both 3 units tall.
# Now Player 1 has only one move
# Plaver 1 removes 2 pieces leaving 1. Towers are 1 and 2 units tall.
# Player 2 matches again. Towers are both 1 unit tall.
# Player 1 has no move and loses. Return 2
# Function Description
#
# Complete the towerBreakers function in the editor below.
#
# towerBreakers has the following paramter(s):
#
# int n: the number of towers
# int m: the height of each tower
# Returns
#
# int: the winner of the game
# Input Format
#
# The first line contains a single integer , the number of test cases.
# Each of the next  lines describes a test case in the form of  space-separated integers,  and .
#
# '''
#
#
# def towerBreakers(n, m):
#     # Write your code here
#     towers = [m, m] if n % 2 == 0 else [m]
#     player1 = 0
#     player2 = 1 if n % 2 == 0 else 0
#     start = 0
#
#     while start < m:
#
#         if towers[player1] <= 1:
#             return 2
#
#         # player1
#         removePiecesFromTower(towers, player1)
#
#         if towers[player2] <= 1:
#             return 1
#
#         # player2
#         removePiecesFromTower(towers, player2)
#
#         start += 1
#
#
# def removePiecesFromTower(towers, player):
#     t = towers[player]
#     store = {}
#
#     val_to_sub = t // 2
#     evenlyDivides(store, val_to_sub, t)
#     val_to_sub = t - 1
#     evenlyDivides(store, val_to_sub, t)
#
#     r = getOptiomal(store)
#     towers[player] = t - r
#
#
# def evenlyDivides(store, val, x):
#     if val > 0 and x % (x - val) == 0:
#         store[val] = x - val
#
#
# def getOptiomal(store):
#     if len(store) >= 1:
#         return max(store)
#
#     return 0
#
# '''
# Declare a 2-dimensional array, , of  empty arrays. All arrays are zero indexed.
# Declare an integer, , and initialize it to .
#
# There are  types of queries, given as an array of strings for you to parse:
# 1. Query: 1 x y
# 1. Let ida = ( (a # last Answer) % n).
# 2. Append the integer y to arrlida.
# 2. Query: 2 x y
# 1. Letida = ( (a @ last Answer) % n).
# 2. Assign the value arrlid.ly % size(arrlida))| to last Answer.
# 3. Store the new value of last Answer to an answers array.
# Query: 1 x y
# Let .
# Append the integer  to .
# Query: 2 x y
# Let .
# Assign the value  to .
# Store the new value of  to an answers array.
# Note:  is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on Wikipedia.  is the modulo operator.
# Finally, size(arr[idx]) is the number of elements in arr[idx]
#
# Function Description
#
# Complete the dynamicArray function below.
#
# dynamicArray has the following parameters:
# - int n: the number of empty arrays to initialize in
# - string queries[q]: query strings that contain 3 space-separated integers
#
# Returns
#
# int[]: the results of each type 2 query in the order they are presented'''
#
# def dynamicArray(n, queries):
#     # Write your code here
#     arr = [[] for _ in range(n)]
#     lastAnswer = 0
#     lastAnswers = []
#
#     for query in queries:
#         a, x, y = query
#         print(query)
#         if int(a) == 1:
#             idx = (x ^ lastAnswer) % n
#             arr[idx].append(y)
#
#         else:
#             idx = (x ^ lastAnswer) % n
#             k = y % len(arr[idx])
#             lastAnswer = arr[idx][k]
#             lastAnswers.append(lastAnswer)
#
#     return lastAnswers
#
#
#
# '''
# In this challenge, the task is to debug the existing code to successfully execute all provided test files.
#
# Given two dates each in the format dd-mm-yyyy, you have to find the number of lucky dates between them (inclusive). To see if a date is lucky,
#
# Firstly, sequentially concatenate the date, month and year, into a new integer  erasing the leading zeroes.
# Now if  is divisible by either  or , then we call the date a lucky date.
# For example, let's take the date "02-08-2024". After concatenating the day, month and year, we get  = 2082024. As  is divisible by  so the date "02-08-2024" is called a lucky date.
#
# Debug the given function findPrimeDates and/or other lines of code, to find the correct lucky dates from the given input.
#
# Note: You can modify at most five lines in the given code and you cannot add or remove lines to the code.
#
# To restore the original code, click on the icon to the right of the language selector.
#
# Input Format
#
# The only line of the input contains two strings  and  denoting the two dates following the format dd-mm-yyyy. Consider,  is the day number,  is the month number and  is the year number.
#
# Note: Here  means January,  means February, means March and so on and all the dates follow the standard structure of English calender including the leap year.
#
# 02-08-2025 04-09-2025
#
# '''
#
# import re
# month = []
#
# def updateLeapYear(year):
#     if year % 400 == 0:
#         month[2] = 29
#     elif year % 100 == 0:
#         month[2] = 28
#     elif year % 4 == 0:
#         month[2] = 29
#     else:
#         month[2] = 28
#
# def storeMonth():
#     month[1] = 31
#     month[2] = 28
#     month[3] = 31
#     month[4] = 30
#     month[5] = 31
#     month[6] = 30
#     month[7] = 31
#     month[8] = 31
#     month[9] = 30
#     month[10] = 31
#     month[11] = 30
#     month[12] = 31
#
# def findPrimeDates(d1, m1, y1, d2, m2, y2):
#     storeMonth()
#     result = 0
#
#     while(True):
#         x = d1
#         x = x * 100 + m1
#         x = x * 10000 + y1
#         if x % 4 == 0 or x % 7 == 0:
#             result = result + 1
#         if d1 == d2 and m1 == m2 and y1 == y2:
#             break
#         updateLeapYear(y1)
#         d1 = d1 + 1
#         if d1 > month[m1]:
#             m1 = m1 + 1
#             d1 = 1
#             if m1 > 12:
#                 y1 =  y1 + 1
#                 m1 = 1
#     return result;
#
# for i in range(1, 15):
#     month.append(31)
#
# line = input()
# date = re.split('-| ', line)
# d1 = int(date[0])
# m1 = int(date[1])
# y1 = int(date[2])
# d2 = int(date[3])
# m2 = int(date[4])
# y2 = int(date[5])
#
# result = findPrimeDates(d1, m1, y1, d2, m2, y2)
# print(result)


# def calculateString(a, b):
#     s1 = len(a)
#     s2 = len(b)
#     results = [0 for _ in range(s2)]
#     if a[0] == b[0]:
#         results[0] = 1
#     result = float('inf')
#
#     for i in range(0, s1):
#         print(results, i)
#         if a[i] == b[0]:
#             results[0] = 1
#         for j in range(1, s2):
#             if a[i] == b[j]:
#                 results[j] = results[j - 1] + 1
#             else:
#                 results[j] = results[j-1]
#
#         result = min(result, results[-1])
#
#     return result

# def calculateString(a, b):
#     s1 = len(a)
#     s2 = len(b)
#     stores = {}
#     result = float('inf')
#     for i in b:
#         val = stores.get(i, 0)
#         stores[i] = val + 1
#
#     for x in a:
#         val = stores.get(x, 0)
#         result = min(result, val)
#
#     return result
#
#
# a = 'abc'
# b = 'abccba'
# a = 'ab'
# b = 'abcbcb'
# a ='za'
# b = 'bzc'
# a = "abcde"
# b= "edbcaacbdebcedaadbecadbceecabddbaecabecdcdabeabcde"
# # a = "abc"
# # b = "xyz"
# val = calculateString(a, b)
#
# print(val)

# def validBracketSequence(sequence):
#     size = len(sequence)
#     stores = {'[' : ']', '{' : '}', '(' : ')', ']' : '[', '}' : '{', ')' : '('}
#     same_direction = False
#
#     if sequence[0] == stores.get(sequence[1]):
#         same_direction = True
#         left = 0
#     else:
#         left = size//2 - 1
#
#     right = left + 1
#
#     # print(same_direction, left)
#     if same_direction:
#         return sameDirections(sequence, left, right, stores)
#     else:
#         return diffDirection(sequence, left, right, stores)
#
#
# def diffDirection(sequences, left, right, stores):
#     size = len(sequences)
#     while left >= 0 and right < size:
#         leftVal = sequences[left]
#         rightVal = sequences[right]
#
#         if leftVal != stores.get(rightVal):
#             return False
#
#         left -= 1
#         right += 1
#
#     return True
#
#
# def sameDirections(sequences, left, right, stores):
#     size = len(sequences)
#     # print('size: ', size)
#     while left < size and right < size:
#         leftVal = sequences[left]
#         rightVal = sequences[right]
#
#         if leftVal != stores.get(rightVal):
#             return False
#
#         left += 2
#         right += 2
#
#     return True
#
# sequence = "{[]}"
# # sequence = "()"
# # sequence = "[]"
# # sequence = "([)]"
# # sequence = "()[]{}"
# sequence = "[][{](})"
#
# val = validBracketSequence(sequence)
# print((val))

# def minDistance(coordinates):
#     size = len(coordinates)
#     coordinates = sorted(coordinates)
#     minDist = float('inf')
#
#     for i in range(1, size):
#         p1 = coordinates[i - 1]
#         p2 = coordinates[i]
#
#         val = calculateEuclideanDistance(p1, p2)
#         minDist = min(minDist, val)
#
#     return minDist
#
#
# def calculateEuclideanDistance(p1, p2):
#
#     return math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))
#
#
# coordinates = [[0, 11], [-7, 1], [-5, -3]]
# coordinates = [[-12,3], [32,29], [-3,-8], [22, -6], [8,26], [14,13], [1,20], [25,27], [23,-9], [25,27],
#              [-1, 33], [31,-10], [25,14]]
# coordinates = [[-4,26], [30,27] , [12,21], [26,-11], [-13,-12]]
# coordinates = [[19,-15], [4,9], [13,-7], [-3,-1], [-10,30]]
# coordinates = [[-5, -6], [9, 22], [33,18], [30,26], [-13,-15], [26,21], [9,5], [31,6]]
# val = minDistance(coordinates)
# print(val)

# def deCompress(compressedString):
#     size = len(compressedString)
#     store = [1]
#     i = 0
#
#     while i < size:
#         char = compressedString[i]
#         prev_char = compressedString[i-1] if i > 0 else ''
#
#         if char.isdigit():
#             if prev_char.isdigit():
#                 store[-1] = store[-1] + char
#             else:
#                 store.append(char)
#
#         elif char == '[':
#             new_array = []
#             x = compressedString[i]
#
#             while x != ']':
#                 i += 1
#                 x = compressedString[i]
#
#                 if x != '[' and x != ']':
#                     new_array.append(x)
#
#             extractChar(new_array, store)
#
#         elif char.isalpha():
#             store.append(char)
#         # print('i:', i)
#         i = i + 1
#
#     print(store)
#     new_string = ''
#     if str(store[0]).isdigit():
#         new_string = ''.join(store[1:])
#         new_string *= int(store[0])
#
#     else:
#         new_string = ''.join(store)
#
#     # print(new_string)
#     return new_string
#
#
# def extractChar(array, store):
#     if array:
#         if array and array[0].isdigit():
#             new_string = ''.join(array[1:])
#             multiplier = int(array[0])
#             store.append(new_string * int(multiplier))
#         else:
#             new_string = ''.join(array)
#             multiplier = store[-1]
#             store[-1] = new_string * int(multiplier)
#
# compressedString = "3[abc]4[ab]c"
# compressedString = "2[3[a]b]"
# # compressedString = "a[]b"
# # compressedString = "10[a]"
# compressedString = "0[abc]"
# val = deCompress(compressedString)
# answer = "abcabcabcababababc"
# answer = "aaabaaab"
# answer = ""
# print(val, val == answer)



# def gcd(A, B):
#     setA = set()
#     setB = set()
#     size = max(A, B)
#
#     left = 1
#
#     while left <= size:
#         if left <= A and A % left == 0:
#             setA.add(left)
#
#         if left <= B and B % left == 0:
#             setB.add(left)
#
#         left += 1
#
#     c = setA.intersection(setB)
#     return max(c) if len(c) > 0 else None
#
#
#     # for i in range(1, A + 1):
#     #     if A % i == 0:
#     #         setA.add(i)
#     #
#     # for i in range(1, B + 1):
#     #     if B % i == 0:
#     #         setB.add(i)
#     #
#     # c = setA.intersection(setB)
#     #
#     # return max(c) if len(c) > 0 else None
#
# A = 6
# B = 4
#
# val = gcd(A, B)
# print(val)

# def countConstruct(target, wordBank, memo={}):
#     if target in memo:
#         return memo[target]
#
#     if target == '':
#         return 1
#
#     total_count = 0
#     for word in wordBank:
#         word_size = len(word)
#         if target[0: word_size] == word:
#             remainder = target[word_size:]
#             vals = countConstruct(remainder, wordBank, memo)
#             total_count += vals
#
#     memo[target] = total_count
#     return total_count
#
# wordBank = ['purp', 'p', 'ur', 'le', 'purpl']
# target = 'purple'
# val = countConstruct(target, wordBank)
# print(val)

# def allConstruct(target, wordBank, memo={}):
#     if target == "":
#         return [[]]
#
#     results = []
#     for word in wordBank:
#         word_size = len(word)
#         if target[0: word_size] == word:
#             remainder = target[word_size:]
#             result = allConstruct(remainder, wordBank, memo)
#             # result = list(map(lambda res: [word] + res, result))
#             result = [[word] + res for res in result]
#             results.extend(result)
#
#     return results
#
#
# wordBank = ['purp', 'p', 'ur', 'le', 'purpl']
# target = 'purple'
# val = allConstruct(target, wordBank)
# print(val)

# def mergeSort(myList : list):
#     s = len(myList)
#     if s == 1:
#         return myList
#
#     m = s // 2
#
#     leftList = myList[: m]
#     rightList = myList[m :]
#
#     left = mergeSort(leftList)
#     right = mergeSort(rightList)
#
#     return merge(left, right)

# def merge(list1, list2):
#
#     s1 = len(list1)
#     s2 = len(list2)
#     x = y = 0
#     merged = []
#     print(list1, list2)
#
#
#     while x < s1 and y < s2:
#         print(merged)
#         if list1[x] < list2[y]:
#             merged.append(list1[x])
#             x += 1
#
#         else:
#             merged.append(list2[y])
#             y += 1
#
#     while x < s1:
#         print(merged)
#         merged.append(list1[x])
#         x += 1
#
#     while y < s2:
#         print(merged)
#         merged.append(list2[y])
#         y += 1
#
#     return merged
#
#
# def mergeSort(myList : list):
#     mid = len(myList) // 2
#     left = myList[:mid]
#     right = myList[mid:]
#
#     merged = []
#     for i in range(len(myList)):
#
#         merged = merge(left, right)
#
#     return merged


# val = mergeSort([1, 4, 6, 3, 7, 5, 2])
# print(val)

# def find_first_last(mylist: list, target):
#     if len(mylist) == 0 or mylist[0] > target or mylist[-1] < target:
#         return [-1, -1]
#     first = find_first(mylist, target)
#     last = find_last(mylist, target)
#
#     return [first, last]
#
#
# def find_first(mylist:list, target):
#     print(mylist)
#     size = len(mylist)
#     start = 0
#     end = size - 1
#
#     # if mylist[0] > target:
#     #     return [-1]
#
#     if size <= 0:
#         return -1
#
#     while start <= end:
#         mid = (start + end) // 2
#         val = mylist[mid]
#         prev_val = mylist[mid - 1] if mid - 1 >= 0 else float('-inf')
#
#         if val == target and prev_val < target:
#             return mid
#
#         elif target <= val:
#             end = mid - 1
#
#         else:
#             start = mid + 1
#
#     return -1
#
#
# def find_last(mylist:list, target):
#     print(mylist)
#     size = len(mylist)
#     start = 0
#     end = size - 1
#
#     while start <= size:
#         mid = (start + end) // 2
#         val = mylist[mid]
#         next_val = mylist[mid + 1] if mid + 1 < size else float('inf')
#
#         if val == target and next_val > target:
#             return mid
#
#         elif target < val:
#             end = mid - 1
#
#         else:
#             start = mid + 1
#
#
#
#     return -1
#
#
# myList = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
# target = 5
#
# vals = find_first_last(myList, target)
# print(vals)


# def createPalindrome(s):
#     size = len(s)
#     leftIdx = 0
#     rightIdx = size - 1
#     potentials = []
#
#     while leftIdx < rightIdx:
#         left = s[leftIdx]
#         right = s[rightIdx]
#
#         if left != right:
#             potentials.append((leftIdx, rightIdx))
#
#         leftIdx += 1
#         rightIdx -= 1
#
#     if potentials:
#         for p in potentials:
#             leftIdx, rightIdx = p
#             sub_left = s[leftIdx + 1: rightIdx + 1]
#             sub_right = s[leftIdx: rightIdx]
#
#             if isPalindrome(sub_left):
#                 return leftIdx
#             if isPalindrome(sub_right):
#                 return rightIdx
#
#     return -1
#
# def isPalindrome(sub):
#     size = len(sub)
#     start = 0
#     end = size - 1
#
#     while start <= end:
#         val_l = sub[start]
#         val_r = sub[end]
#
#         if val_l != val_r:
#             return False
#
#         start += 1
#         end -= 1
#
#     return True
#
#
# s = 'aaab'
# s = 'aaa'
# s = 'baa'
# s = 'bcbc'
#
# val = createPalindrome(s)
# print(val)


# def getTotalX(a, b):
#
#     factors = []
#     for x in range(a[-1], b[0] + a[-1], a[-1]):
#         isValid = True
#         # print(x)
#         for y in a:
#             if x % y != 0:
#                 isValid = False
#
#         for k in b:
#             if k % x != 0:
#                 isValid = False
#
#         if isValid:
#             factors.append(x)
#
#     return len(factors)
#
#
#
#
# a = [2, 4]
# b = [16, 32, 96]
#
# # a = [2, 6]
# # b = [24, 36]
#
# val = getTotalX(a, b)
# print(val)

def anagram(s):
    # Write your code here
    if not s:
        return -1

    size = len(s)
    mid = size // 2

    store1 = {}
    store2 = {}
    s1 = s[:mid]
    s2 = s[mid:]

    if len(s1) != len(s2):
        return -1
    if isAnagram(s1, s2, store1, store2):
        return 0

    changes = findUnbalancedChars(s1, store1, store2)

    return changes


def findUnbalancedChars(s1, store1, store2):
    for i in range(len(s1)):
        char = s1[i]
        idxArray1 = store1.get(char, [])
        idxArray2 = store2.get(char, [])
        if idxArray2:
            idxArray2.pop()
            if not idxArray2:
                store2.pop(char)
            else:
                store2[char] = idxArray2

            idxArray1.pop()
            if not idxArray1:
                store1.pop(char)
            else:
                store1[char] = idxArray1

    return getChanges(store1)

def getChanges(store):
    size = 0
    for k, v in store.items():
        size += len(v)

    return size

def isAnagram(s1, s2, store1, store2):

    for i in range(len(s1)):
        char1 = s1[i]
        char2 = s2[i]
        idxArr1 = store1.get(char1, [])
        idxArr2 = store2.get(char2, [])
        idxArr1.append(i)
        idxArr2.append(i)
        store1[char1] = idxArr1
        store2[char2] = idxArr2

    return store1 == store2


s = 'xaxbbbxx'
s = 'aaabbb'
s = 'abc'
s = 'mnop'
s = 'xyyx'

val = anagram(s)
print(val)














