'''
Question: You are given n eggs and specified a number of k floors. Write an algorithm to find the minimum number of
drops is required to know the floor from which if the egg is dropped, it will break.
'''

def egg_dropping(eggs: int, floors: int) -> int:
    return drop(eggs, floors, floors)

def drop(eggs: int, floors: int, total_floors: int):
    if eggs == 1:
        return floors

    if floors <= 1:
        return floors

    return 1 + max(drop(eggs-1, floors - 1, total_floors), drop(eggs, (total_floors - floors), total_floors))

floors = 2
eggs = 2

res = egg_dropping(eggs, floors)
print(res)