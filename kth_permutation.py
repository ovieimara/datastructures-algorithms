
def kth_permutation(n, k):
    permutation = []
    unused = [i for i in range(1, 5)]
    fact = [1] * n + 1
    for i in range(1, n + 1):
        fact[i] = i * fact[i-1]

    k =- 1

    while n > 0:
        part_length = fact[n] // n
        i = k // part_length
        permutation.append(unused[i])
