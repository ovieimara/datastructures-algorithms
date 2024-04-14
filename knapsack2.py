
def knap(i, v, w, k):
    if i == len(v):
        return 0

    if k < 0:
        return float("-inf")

    return max(v[i] + knap(i+1, v, w, k - w[i]), knap(i+1, v, w, k))
def knapsack(v, w, k):
    return knap(0, v, w, k)

    sack = [float("-inf")] * (k + 1)
    sack[0] = 0

    for i in range(1, k+1):
        # max_val = float("-inf")
        for j in range(0, len(w)):
            if i >= w[j]:
                sack[i] = max(sack[i], v[j] + sack[i - w[j]])

        print(sack)
    return sack[-1]

v = [2, 3, 1, 2, 4]
w = [4, 3, 5, 1, 2]
k = 5

# v = [20, 30, 15, 25, 10]
# w = [6, 13, 7, 10, 3]
# k = 20

print(knapsack(v, w, k))