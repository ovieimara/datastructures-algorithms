

def arrayManipulation(n, queries):

    result = [0] * n
    for query in queries:
        x, y, z = query
        result[x-1] += z
        result[y-1] -= z

    max_val = 0
    for i in range(1, len(result)):
        result[i] += result[i-1]
        max_val = max(max_val, result[i])

    return max_val

queries = [[1,5,3], [4,8,7], [6,9,1]]
# queries = [[1,2,100], [2,5,100], [3,4,100]]
n = 10
# n = 5
res = arrayManipulation(n, queries)
print(res)