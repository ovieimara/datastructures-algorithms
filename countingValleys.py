def countingValleys(steps, path):
    # Write your code here
    valley = 0
    stack = []
    for i in range(steps):
        step = path[i]
        if not stack:
            stack.append(step)
            continue
        if step == stack[-1]:
            stack.append(step)
        else:
            val = stack.pop()
            if val == 'D' and not stack:
                valley += 1

    return valley

steps = 8
path = "UDDDUDUU"

res = countingValleys(steps, path)