
from collections import deque
def reachLastIndex(arr: list):
    adj = {}
    for i in range(len(arr)):
        adj[i] = []
        for j in range(1, arr[i] + 1):
            if i + j < len(arr):
                adj[i].append(i + j)
    print(adj)
    return bfs(adj, arr, 0)

def bfs(adjacencyList: dict, arr:list, startIndex: int):
    queue = deque([startIndex])
    visited = {startIndex}
    while queue:
        vertex = queue.popleft()
        if vertex == len(arr) - 1:
            return True
        print(vertex, startIndex, visited)

        if startIndex != 0 and vertex in visited:
            continue

        for neighbor in adjacencyList[vertex]:
            # if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return False


arr = [3, 0, 2, 0, 2, 1, 4, 3]
result = reachLastIndex(arr)
print(result)