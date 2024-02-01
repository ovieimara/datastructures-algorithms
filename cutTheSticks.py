def cutTheSticks(arr):
    # Write your code here
    cut_size = min(arr)
    size = n = len(arr)
    res = []

    while n:
        potential_cut_size = float('inf')
        res.append(n)
        for j in range(size):
            if arr[j] > 0 and arr[j] >= cut_size:
                arr[j] -= cut_size
                if arr[j] == 0:
                    n -= 1
                if arr[j] > 0:
                    potential_cut_size = min(potential_cut_size, arr[j])
        cut_size = potential_cut_size

    return res


'''
6
5 4 4 2 2 8
'''