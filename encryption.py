import math
from typing import Tuple
def encryption(s: str):
    # Write your code here
    new_s = s.replace(" ", '')
    n = len(new_s)
    row, col = row_col(n)
    r, c = row, col
    if row * col < n:
        r, c = col, col
    return encrypt(new_s, r, c, n)

def row_col(n: int) -> Tuple[int, int]:
    root = math.sqrt(n)
    row = math.floor(root)
    col = math.ceil(root)

    return row, col

def encrypt(s, rows, cols, n):
    sentence = []
    for i in range(cols):
        word = [s[j] for j in range(i, n, rows + 1 if rows != cols else rows)]
        sentence.append(''.join(word))
    return ' '.join(sentence)
def find_min(row, col, n):
    a = (row, col)
    b = (col, col)

    r, c = min(a, b, key=lambda x : x[0] * x[1])
    return (r, c) if r * c >= n and (r, c) == a else (col, col)

string = "haveaniceday"
# string = "feedthedog"
string = "chillout"
string = "if man was meant to stay on the ground god would have given us roots"
print(encryption(string))


