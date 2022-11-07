#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    sorted(unsorted, key=int)
    return sort(0, len(unsorted), unsorted)

def sort(start, end, arr):
    # print(end - start)
    if end - start == 1:
        return arr[start:end]

    mid = (start + end) // 2
    return mergeSort(sort(start, mid, arr), sort(mid, end, arr))

def mergeSort(left, right):
    l = 0
    r = 0
    arr = []
    print(left, right)
    while l < len(left) and r < len(right):
        if int(left[l]) <= int(right[r]):
            arr.append(left[l])
            l += 1

        elif int(left[l]) > int(right[r]):
            arr.append(right[r])
            r += 1

    while l < len(left):
        arr.append(left[l])
        l += 1

    while r < len(right):
        arr.append(right[r])
        r += 1

    return arr

unsorted = [500, 5, 3, 4, 1, 2]
unsorted = ['1', '200', '50', '3']
val = bigSorting(unsorted)
print(val)