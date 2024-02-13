from collections import defaultdict

def minimumDistances(a):
    # pairs = defaultdict(lambda : list)
    pairs ={}
    min_distance = float("inf")
    for i, ele in enumerate(a):
        idxs = pairs.get(ele, [])
        if idxs:
            min_distance = min(min_distance, i - idxs[0])

        idxs.append(i)
        pairs[ele] = idxs

    return min_distance if min_distance != float('inf') else -1


arr = [7, 1, 3, 4, 1, 7]
arr = [3, 2, 1, 2, 3]
print(minimumDistances(arr))
