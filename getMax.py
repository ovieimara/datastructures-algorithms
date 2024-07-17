

def getMax(operations):
    stack = []
    result = []

    for ops in operations:
        query = ops.split()
        y = int(query[0])
        x = int(query[1]) if len(query) > 1 else ''
        if y == 1:
            if stack and stack[-1] > x:
                stack.append(stack[-1])
            else:
                stack.append(x)

        elif stack and y == 2:
            stack.pop()
        else:
            result.append(stack[-1])

    return result

operations = ['1 97', '2', '1 20', '1 26', '1 20', '2', '3', '1 91', '3']
res = getMax(operations)
print(res)