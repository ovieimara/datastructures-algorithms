def lilysHomework(arr):
    # Write your code here
    size = len(arr)
    count = 0
    result = [0] * size
    store = [0, 0]
    table = []

    for i in range(1, 3):
        store[i - 1] = abs(arr[i] - arr[i - 1])

    if store[1] < store[0]:
        table = sorted(arr)
    else:
        table = sorted(arr, reverse=True)
        # return count
    print(table)
    isSorted = False
    count = 0

    while not isSorted:
        l = 0
        r = size - 1
        # print(l, size, arr[l], table[l])
        while l < size and arr[l] == table[l]:
            l += 1
        print(l, size - 1)
        while r >= 0 and arr[r] == table[r]:
            r -= 1

        if l < size and r >= 0:
            swap(l, r, arr)
            count += 1

        if l >= size or r <= 0:
            isSorted = True

        l += 1
        r -= 1

    return count

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

arr = [2, 5, 3, 1]
arr = [7, 15, 12, 3]
arr = [3, 4, 2, 5, 1]
res = lilysHomework(arr)
print(res)