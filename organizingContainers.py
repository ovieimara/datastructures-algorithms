from typing import List
def organizingContainers(container: List):
    n = len(container)
    row_total = [sum(c) for c in container]
    col_total = [sum(c[i] for c in container) for i in range(n)]

    return "Possible" if sorted(row_total) == sorted(col_total) else "Impossible"

container = [[1, 4], [2, 3]]
container = [[1, 1], [1, 1]]
container = [[0, 2], [1, 1]]
container = [[1, 3, 1], [2, 1, 2], [3, 3, 3]]
container = [[0, 2, 1], [1, 1, 1], [2, 0, 0]]
print(organizingContainers(container))