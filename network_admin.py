from typing import List


def solve(links, queries):
    # Write your code here

    for query in queries:
        q, server_a, server_b, val = query
        server_index = isExist(server_a, server_b, links)
        # print(links[server_index])

        servers = links[server_index] if server_index >= 0 else [-1, -1, -1]
        server_A, server_B, admin = servers

        if q == 1:

            if server_index < 0:
                print("Wrong link")
                continue

            elif server_index >= 0 and admin == val:
                # server_A, server_B, admin = links[server_index]
                # if admin == val:
                print('Already controlled link')
                continue

            elif isOverLoad(server_a, server_b, val, links) >= 0:
                print('Server overload')
                continue

            elif admin == val:
                print('Network redundancy')
                continue


            links[server_index][2] = val
            print('Assignment done')

        if q == 2:
            links[server_index][2] = val

        elif q == 3:
            if server_index < 0:
                print('No connection')
            elif links[server_index][2] == val:
                print(f"{links[server_index][2]} security devices placed")

    return ''

def isOverLoad(server_a: int, server_b: int, admin: int, links: List) -> int:
    for i in range(len(links)):
        server_A, server_B, assign = links[i]
        if (server_A == server_a and assign >= 2 and assign == admin) or (server_B == server_b and assign >= 2 and assign == admin):
            return i

    return -1


def isExist(server_a: int, server_b: int, links: List) -> int:
    for i in range(len(links)):
        server_A, server_B, assign = links[i]
        if server_A == server_a and server_B == server_b:
            return i

    return -1



links = [
    [1, 2, 1],
    [2, 3, 1],
    [3, 4, 2],
    [1, 4, 2],
    [1, 3, 3],

]
queries = [
    [1, 1, 2, 3],
    [2, 1, 4, 64],
    [3, 1, 4, 2],
    [1, 1, 2, 3],
    [3, 4, 2, 3],
    [3, 1, 3, 3],
    [1, 1, 4, 3],
    [3, 3, 4, 2],
    [3, 2, 4, 1],
    [2, 1, 4, 13],
    [2, 1, 3, 21],
    [2, 2, 3, 24],
    [1, 2, 3, 3],
    [1, 2, 4, 3]
]

res = solve(links, queries)
print(res)