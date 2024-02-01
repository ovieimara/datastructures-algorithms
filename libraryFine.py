def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here

    is_same_year = y2 == y1
    is_same_month = m2 == m1
    diff_months = m1 - m2
    diff_days = days(is_same_month, is_same_year, d1, d2, m2, y2)

    if y2 > y1:
        return 0

    if m2 > m1 and is_same_year:
        return 0

    if d2 >= d1 and is_same_year and is_same_month:
        return 0

    if is_same_year and is_same_month:
        return 15 * diff_days

    if is_same_month and not is_same_year:
        return 10000

    if is_same_year and not is_same_month:
        return 500 * diff_months

    if not is_same_year and not is_same_month:
        return 10000


def days(is_same_month, is_same_year, d1, d2, m2, y2):
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    is_leap_year2 = is_leap_year(y2)
    diff_days = 0

    if m2 == 2 and is_leap_year2:
        diff_days = (29 - d2) + d1

    elif is_same_month and is_same_year:
        diff_days = abs(d2 - d1)
    else:
        diff_days = (months.get(m2) - d2) + d1

    return diff_days


def is_leap_year(year):
    # Leap years are divisible by 400
    if year % 400 == 0:
        return True
    return False



'''
return = 9 6 2015
due = 6 6 2015
'''