def equalizeArray(arr):
    arr.sort()
    if len(arr) < 2:
        return 0

    i = 0
    total = 0
    while i < len(arr):
        count = 1
        i += 1
        while i < len(arr) and arr[i] == arr[i-1]:
            count += 1
            i+= 1
        if total < count:
            total = count

    return len(arr) - total




array = [1, 2, 2, 3]
# array = [3, 3, 2, 1, 3]
# array = [1, 2, 3, 1, 2, 3, 3, 3]

res = equalizeArray(array)
print(res)