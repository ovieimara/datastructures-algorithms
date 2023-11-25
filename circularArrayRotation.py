#complexity: Time: O(n), space = O(n)
def circularArrayRotation(a, k, queries):
    # Write your code here
    n = len(a)
    pointer = (n - k) % n

    return [a[(q + pointer) % n] for q in queries]

#complexity: Time: O(n), space = O(n)
# def circularArrayRotation

    # final_state = [0] * n

    # for i in range(n):
    #     final_state[(i + k) % n] = a[i]

    # return [final_state[q] for q in queries]