def arrayManipulation(n, queries):
    # Write your code here
    # array = [queries[0][2] if queries[0][0] - 1 <= i < queries[0][1] else 0 for i in range(n)]
    # print(array)
    array = [0] * n
    rows = len(queries)
    max_value = [float('-inf')]

    results = list(map(lambda query: update(query, array, max_value), queries))
    print(list(results))
    return list(results)[-1]

    # for i in range(1, rows):
    #     leftIdx = queries[i][0]
    #     rightIdx = queries[i][1]
    #     query = queries[i][2]
    #
    #     for j in range(leftIdx - 1, rightIdx):
    #         array[j] += query
    #
    #         maxValue = max(maxValue, array[j])
    #
    # return maxValue


def update(query, array, max_value):
    left_idx, right_idx, q = query
    # print(left_idx, right_idx, q)

    for j in range(left_idx - 1, right_idx):
        array[j] += q

        max_value[0] = max(max_value[0], array[j])
        print(array)
    return max_value[0]


queries = [[1,5,3], [4,8,7], [6,9,1]]
# queries = [[1,2,100], [2,5,100], [3,4,100]]
n = 10
# n = 5
res = arrayManipulation(n, queries)
print(res)