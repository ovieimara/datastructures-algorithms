'''
Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed
edges times[i] = (ui, vi, wi), where Ui is the source node, Vi is the target node and Wi is the time it takes for a
signal to travel from source to target.
We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. if it is impossible for all
n nodes to receive the signal, return -1

input: times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], n = 4, k = 2
output: 2
'''
import heapq
from typing import  List
from collections import defaultdict
def delay(times: List, n: int, k: int):
    edges = defaultdict(list)

    for u, v, w in times:
        edges[u].append((v, w))

    print(edges)
    heap = [(0, k)]
    visited = {k}
    t = 0

    while heap:
        time, node = heapq.heappop(heap)
        t = max(t, time)

        for vertex, weight  in edges[node]:
            if vertex not in visited:
                heapq.heappush(heap, (time+weight, vertex))
                visited.add(vertex)

    print(visited)
    return t if len(visited) == n else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

res = delay(times, n, k)
print(res)