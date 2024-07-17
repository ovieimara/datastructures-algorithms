
def equalStacks(h1, h2, h3):
    # Write your code here
    stacks_set = [set() for _ in range(3)]
    stacks = [h1, h2, h3]

    for i, stack in enumerate(stacks):
        cumm = 0
        stacks_set[i].add(cumm)
        for num in stack[:: -1]:
            cumm += num
            stacks_set[i].add(cumm)

    print(stacks_set)
    sizes = set.intersection(*stacks_set)

    return max(sizes)

h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]

res = equalStacks(h1, h2, h3)
print(res)


