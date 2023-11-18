def dayOfProgrammer(year):
    # Write your code here
    num = ''
    if year == 1918:
        return f"{26}.09.{year}"

    if isLeapYear(year):
        num = 256 - 244
    else:
        num = 256 - 243

    return f"{num}.09.{year}"


def isLeapYear(year):
    if year > 1918:
        if (year % 4 == 0 and year % 100 > 0) or year % 400 == 0:
            return True
    if year < 1918:
        if year % 4 == 0:
            return True

    return False

res = dayOfProgrammer(2016)
print(res)