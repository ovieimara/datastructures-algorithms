def maxProfit(arr):
    n = len(arr)
    # arr.append(float('inf'))
    start = 0
    end = n
    max_val = float('-inf')
    count = 0
    left = 0
    right = 1
    while right <= len(arr) + 1:
        sub = arr[left : right]
        print(sub)
        max_val = max(max_val, max(sub))
        is_profitable = sub[0] >= max_val or sub[-1] >= max_val
        # if is_profitable:
        count += 1
        if right < n:
            if arr[right] >= max_val or arr[left] >= max_val:
                right += 1
            else:
                left += 1
        else:
            right+=1
            left+=1

        print(left, right)


    print(count)

# arrays = [2, 3, 2]
array = [3, 1, 3, 5]
maxProfit(array)