import math

def workbook(n, k, arr):
    # Write your code here
    count = 0
    page = 1

    start = 1
    pages_chapter = [math.ceil(arr[i] / k) for i in range(n)]
    # last_pages = [arr[i] % k if arr[i] % k > 0 else k for i in range(n)]
    # each_pages = [min(arr[i], k) for i in range(n)]

    # end_pages = [0] * n
    # end_pages[0] = start + each_pages[0]
    #
    # for i in range(1, n):
    #     end_pages[i] = end_pages[i-1] + each_pages[i]

    x = 0
    i = 0
    res = []
    # while x < pages_chapter[i] - 1:
    #     res.append({*range(start, end)})
    #     start = end
    #     end = start + each_page
    #     x += 1

    for i in range(n):
        last_page = arr[i] % k if arr[i] % k > 0 else k
        each_page = min(arr[i], k)
        start = 1
        end = start + each_page
        res = []
        x = 0
        while x < pages_chapter[i] - 1:
            res.append({*range(start, end)})
            start = end
            end = start + each_page
            x+=1

        res.append({*range(start, start+last_page)})
        y = 0
        while y < len(res):
            count += int(page in res[y])
            y += 1
            page += 1


    return count

n = 5
k = 3
arr = [4, 2, 6, 1, 10]
n = 2
k = 3
arr = [4, 2]
print(workbook(n, k, arr))




