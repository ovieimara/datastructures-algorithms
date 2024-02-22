

def cavityMap(grid):
    '''
    i = 0 ineligible
    i = len(grid) - 1 ineligible
    j = 0 ineligible
    j = len(grid[0]) - i ineligible
    :param grid:
    :return:
    '''
    row = len(grid)
    col = len(grid[0])
    char = 'X'
    new_grid = [[0 for i in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            new_grid[i][j] = grid[i][j]
        if i == 0 or i == row - 1:
            new_grid[i] = ''.join(new_grid[i])


    for i in range(1, row-1):
        for j in range(1, col-1):
            max_cell = max(grid[i-1][j], grid[i][j-1], grid[i][j+1], grid[i+1][j])
            if grid[i][j] > max_cell:
                new_grid[i][j] = char
        new_grid[i] = ''.join(new_grid[i])

    return new_grid

grid = ['1112',
        '1912',
        '1892',
        '1234']

# grid = ['989', '191', '111']

print(cavityMap(grid))

