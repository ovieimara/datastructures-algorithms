
def find_min(arr, array):
    return min(arr, key=lambda x : array[x] if x < len(array) else float('inf'))

array = [6, 5, 1, 7, 3, 2, 4]
arr = [0, 70]

print(find_min(arr, array))