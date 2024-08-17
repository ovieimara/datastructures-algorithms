

def waysToDecode(string: str):
    return decode(string, 0)

def decode(string: str, i: int) -> int:
    if i >= len(string)-1:
        return 1

    if (0 < int(string[:1]) <= 9) and (10 <= int(string[:2]) < 27):
        return decode(string, i + 1) + decode(string, i + 2)

    if (0 < int(string[:1]) <= 9):
        return decode(string, i + i)

    return 0

string = "12"
string = "2263"
string = "10"
string = "101"
string = "226"
res = waysToDecode(string)
print(res)