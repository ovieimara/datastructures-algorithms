from collections import deque

def hackerlandRadioTransmitters(x, k):
    numOfRadios = 0
    x.sort()
    queue = deque(x)

    while queue:
        left = right = queue.popleft()
        print(left, len(queue))
        while queue and queue[0] <= left + k:
            right = queue.popleft()
        while queue and queue[0] <= right + k:
            queue.popleft()
        numOfRadios += 1
    return numOfRadios

x = [1, 2, 3, 4, 5]
k = 1

res = hackerlandRadioTransmitters(x, k)
print(res)