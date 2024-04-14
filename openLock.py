from collections import deque

def openLock(state, deadends, target):
    queue = deque()
    queue.append((state, 0))
    visited = {state}
    deadend = set(deadends)

    while queue:
        vertex, level = queue.popleft()

        if vertex == target:
            return level

        for i in range(len(vertex)):
            wheel = vertex[i]
            up = (int(wheel) + 1) % 10
            down = (int(wheel) - 1) % 10

            turn_up = vertex[ : i] + str(up) + vertex[i + 1 : ]
            turn_down = vertex[: i] + str(down) + vertex[i + 1:]

            if turn_up not in deadend and turn_up not in visited:
                queue.append((turn_up, level+1))
                visited.add(turn_up)
            if turn_down not in deadend and turn_down not in visited:
                queue.append((turn_down, level+1))
                visited.add(turn_down)

    return -1


state = "0000"
deadends = ['0201', '0101', '0102', '1212', '2002']
target = "0202"

print(openLock(state, deadends, target))