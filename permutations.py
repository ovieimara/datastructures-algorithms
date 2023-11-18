def getPermutations(arr):
    if len(arr) < 2:
        return [arr]

    permutations = []
    for i in range(len(arr)):
        remaining = arr.copy()
        remaining.pop(i)
        remaining_permutations = getPermutations(remaining)
        removed_element = [arr[i]]

        for permutation in remaining_permutations:
            permutations.append(removed_element + permutation)

    return permutations


# val = getPermutations([1, 2])
val = getPermutations([1, 2, 3, 4])

print(val)
