

def solve(arr, queries):
    result = []
    for q in queries:
        smallest = solveSubArray(arr, q)
        result.append(smallest)

    return result


def solveSubArray(arr, q):
    size = len(arr)
    i = 0
    smallest = float('inf')

    while i <= size - q:
        largest = float('-inf')
        for j in range(i, i + q):
            largest = max(largest, arr[j])

        smallest = min(smallest, largest)
        i += 1

    return smallest

arr = [1, 2, 3, 4, 5]
queries = [1, 2, 3, 4, 5]
res = solve(arr, queries)
print(res)