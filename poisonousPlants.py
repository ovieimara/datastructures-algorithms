from copy import deepcopy


def poisonousPlants(p):
    # Write your code here
    stack = []
    max_days = 0
    for i in range(len(p) - 1, -1, -1):
        days = 0
        while stack and p[i] < stack[-1][0]:
            days = max(days + 1, stack[-1][1])
            stack.pop()

        stack.append((p[i], days))
        max_days = max(max_days, days)

    return max_days


p = [3, 6, 2, 7, 5]
p = [6, 5, 8, 4, 7, 10, 9]

res = poisonousPlants(p)
print(res)





