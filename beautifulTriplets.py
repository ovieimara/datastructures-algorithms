

def beautifulTriplets(d, arr):
    arr_set = set(arr)
    count = 0
    for ele in arr:
        next_ = ele + d
        next_next = next_ + d

        if next_ in arr_set and next_next in arr_set:
            count += 1

    return count

def triplets(arr, d):
    i = 0
    result = 0

    while i < len(arr) - 2:
        j = i + 1
        k = len(arr) - 1
        while j < len(arr) - 1 and k >= 0 and i < j < k:
            if (arr[j] - arr[i]) == (arr[k] - arr[j]) == d:
                # result.append([i, j, k])
                result += 1
                j += 1
                k -= 1
            else:
                updated = False
                if (arr[j] - arr[i]) < d:
                    j += 1
                    continue

                if (arr[k] - arr[j]) > d:
                    k -= 1
                    continue

                # if not updated:
                j += 1
                k -= 1

        i += 1

    return result





# def triplets(arr, d, i, subset, result):
#     if i >= len(arr) - 1:
#         return
#     if len(subset) == 3:
#         x, y, z = subset
#         if arr[y] - arr[x] == d and arr[z] - arr[y] == d:
#             result.append(subset)
#
#     if subset[-1] >= i:
#         triplets(arr, d, i + 1, subset, result)
#
#     triplets(arr, d, i + 1, subset + [i], result)
#     triplets(arr, d, i + 1, subset, result)

d = 1
arr = [2, 2, 3, 4, 5]

# d = 3
# arr = [1, 2, 4, 5, 7, 8, 10]
print(beautifulTriplets(d, arr))

