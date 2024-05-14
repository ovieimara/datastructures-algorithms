
def bomberMan(n, grid):
    # Write your code here
    rows = len(grid)
    cols = len(grid[0])
    full_grid = [ ['O']*cols for _ in range(rows) ]

    if n == 1:
        return grid

    if n % 2 == 0:
        return list(map(lambda row: ''.join(row), full_grid))

    processed_grid = detonate(grid)

    if n == 3 or n % 4 == 3:
        return processed_grid

    if n % 4 == 1:
        return detonate(processed_grid)

def detonate(grid):
    clear = '.'
    bomb = 'O'
    rows = len(grid)
    cols = len(grid[0])
    last_grid = [ [bomb]*cols for _ in range(rows) ]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == bomb:
                if last_grid[i][j] != clear:
                    last_grid[i][j] = clear

                if i+1 < rows and last_grid[i+1][j] != clear:
                    last_grid[i+1][j] = clear

                if j+1 < cols and last_grid[i][j+1] != clear:
                    last_grid[i][j+1] = clear

                if i-1 >= 0 and last_grid[i-1][j] != clear:
                    last_grid[i-1][j] = clear

                if j-1 >= 0 and last_grid[i][j-1] != clear:
                    last_grid[i][j-1] = clear

    return list(map(lambda r: ''.join(r), last_grid))


grid =['.......',
       '...O...',
       '....O..',
       '.......',
       'OO.....',
       'OO.....'
       ]
n = 9
# grid = ['OOO.OOO', 'OO...OO', 'OOO...O', '..OO.OO', '...OOOO', '...OOOO']
grid = ['.......',
        '...O.O.',
        '....O..',
        '..O....',
        'OO...OO',
        'OO.O...',
        ]
grid = ['OOO.O.O', 'OO.....', 'OO....O', '.......', '.......', '.......']
grid = ['.......', '...O.O.', '...OO..', '..OOOO.', 'OOOOOOO', 'OOOOOOO']
res = bomberMan(n, grid)
print(res)