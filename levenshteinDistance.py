'''
Question: Write a program that takes two strings and computes the minimum number of edits needed to transform the first string into the second string.

Examples:

Input: "Saturday" and "Sundays"
Output: 4

Why:
In: "Saturday"
1.) Delete the first 'a' ("Sturday")
2.) Delete the first 't' ("Surday")
3.) Replace 'r' with 'n' ("Sunday")
4.) Insert an 's' at the end ("Sundays")
Out: "Sundays"

Our 3 Operations To Fix Character Mismatch:
- Insert
- Delete
- Replacement
'''

def editDistance(a, b):
    # return distance(a, b)
    return distance(a, b, 0, 0)

# def distance(a, b):
#     rows = len(b)
#     cols = len(a)
#     table = [[i for i in range(cols+1)] for _ in range(rows+1)]
#
#     for r in range(rows+1):
#         table[r][0] = r
#
#     print(table)
#
#     for i in range(1, rows+1):
#         for j in range(1, cols+1):
#             if b[i-1] == a[j-1]:
#                 table[i][j] = table[i-1][j-1]
#             else:
#                 table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])
#     print(table)
#     return table[-1][-1]


#recursion
def distance(a: str, b: str, i: int, j:int) -> int:
    if j == len(b):
        return len(a) - i
    if i == len(a):
        return len(b) - j

    if a[i] == b[j]:
        return distance(a, b, i+1, j+1)
    else:
        return 1 + min(distance(a, b, i+1, j), distance(a, b, i, j + 1), distance(a, b, i + 1, j + 1))

a = "Saturday"
b = "Sundays"
# a = "benyam"
# b = "ephrem"

res = editDistance(a, b)
print(res)