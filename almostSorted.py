import copy


def almostSorted(arr):
    # Write your code here
    arr_copy = copy.deepcopy(arr)
    sorted_arr = sorted(arr)
    new_arr = [float('-inf')] + arr + [float('inf')]

    sw = rv = False
    i = 1
    while i < len(new_arr) and new_arr[i] > new_arr[i - 1]:
        i += 1

    i -= 2

    j = len(new_arr) - 2
    while j >= 0 and new_arr[j] < new_arr[j + 1]:
        j -= 1

    swap(arr_copy, i, j)
    is_sorted = sorted_arr == arr_copy
    if sorted_arr == arr_copy:
        sw = True
        print('yes')

    if not is_sorted:
        if reverse(arr, i, j, sorted_arr):
            rv = True
            print('yes')

    print_out(sw, rv, i, j)


def print_out(sw, rv, i, j):
    if sw and rv:
        print(f"swap {i + 1} {j + 1}")
    if rv and not sw:
        print(f"reverse {i + 1} {j + 1}")
    if sw and not rv:
        print(f"swap {i + 1} {j + 1}")
    if not sw and not rv:
        print("no")


def reverse(arr, i, j, sorted_arr):
    return sorted_arr == arr[:i] + arr[i:j + 1][-1:: -1] + arr[j + 1:]


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


arr = [4, 2]
arr = [3, 1, 2]
arr = [1, 5, 4, 3, 2, 6]
arr = [1, 5, 4, 3, 2]
arr = [1, 2, 3, 5, 4]
arr = [2, 1, 3, 5, 4]
arr = [2, 1, 3, 4, 5]
arr = [1, 2, 4, 3, 5]
arr = [5, 4, 3, 2, 1]

almostSorted(arr)