

def serviceLane(widths, cases):
    result = []
    for case in cases:
       i, j = case
       result.append(min(widths[i : j+1]))

    return result

widths = [2, 3, 1, 2, 3, 2, 3, 3]
cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]

print(serviceLane(widths, cases))
