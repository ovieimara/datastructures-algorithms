import heapq

x = [3, 7, 1, 2]
y = [8, 5, 3, 4]
z = [1, 4, 9, 6]


arr = [(3, 0, 0), (8, 1, 0), (1, 2, 0)]
heapq.heapify(x)
res = heapq.heappop(x)
print(res)