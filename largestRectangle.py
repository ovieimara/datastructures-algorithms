
def largestRectangle(h):
    size = len(h)
    left = [0] * size
    right = [0] * size
    stack = [0]
    arr = [-1] + h + [-1]


    for i in range(1, len(arr)-1):
        val = arr[i]

        while arr[stack[-1]] >= val:
            stack.pop()

        index = stack[-1]
        left[i-1] = index
        stack.append(i)

    stack = [len(arr) - 1]
    for i in range(len(arr) - 2, 0, -1):
        val = arr[i]
        while arr[stack[-1]] >= val:
            stack.pop()

        index = stack[-1]
        right[i-1] = index
        stack.append(i)

    max_area = 0
    for i in range(len(h)):
        k = left[i] - (right[i] - 1)
        max_area = max(max_area, abs(h[i] * k))

    return max_area

    # h.sort()
    #
    # i = 0
    # j = size - 1
    # mid = size // 2
    #
    # left = h[:mid]
    # right = h[mid:]
    # return max(min(left) * len(left), min(right) * len(right), min(h) * size)


def largest(i, j, h, large):
    mid = (i + j) // 2
    left = min(h[: mid]) * len(h[: mid])
    right = min(h[mid:]) * len(h[mid:])






# def largestRectangle(h):
#     size = len(h)
#     # h.sort()
#
#     i = 0
#     j = size - 1
#     largest = 0
#     while i <= j:
#
#         largest = max(largest, min(h[i: j+1]) * (j - i + 1))
#         if h[i] < h[j]:
#             i += 1
#         else:
#             j -= 1
#
#     return largest
    # return max(len(h[i:]) * min(h[i:]) for i in range(size))

h = [1, 2, 3, 4, 5]
# answer = 9
# h = [8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116]
answer = 26152
# h = [3, 2, 3]
res = largestRectangle(h)
print(res)

h = [-1, 3, 2, 3, -1]
l = [0, 0, 2]
r = [1, 4, 4]
a = [0, 6, 0]



