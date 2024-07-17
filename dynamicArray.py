def dynamicArray(n, queries):
    # Write your code here
    last_answer = 0
    arr = [[] for _ in range(n)]
    answers = []

    for query in queries:
        q, x, y = query
        idx = (x ^ last_answer) % n
        if q == 1:
            arr[idx].append(y)
        else:
            last_answer = arr[idx][y % len(arr[idx])]
            answers.append(last_answer)

    return answers


n = 2
queries = [[1, 0, 5], [1, 1, 7]]
res = dynamicArray(n, queries)
print(res)