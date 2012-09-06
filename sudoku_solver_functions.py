# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

import math

def grid_as_string(grid):
  gridString = ""
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      gridString += str(grid[i][j]) + "\t"
    gridString += "\n"
  return gridString

def parse_string(gridString):
    grid = []
    lines = gridString.split("\n")
    for i in range(len(lines)):
        l = lines[i]
        if (len(l) == 0):
            continue
        grid.append([])
        cells = l.split()
        for c in cells:
            grid[i].append(int(c))
    return grid

def is_correct_grid(grid):
    # Just to be clear:
    # grid[i][j] : cell at line i+1 and column j+1
    # For example : grid[3][5] is...
    #       v
    #  000000000
    #  000000000
    #  000000000
    #  00000X000 <--- right there
    #  000000000
    #  000000000
    #  000000000
    #  000000000
    #  000000000
    
    # Sanity checks
    
    try:
        if (len(grid) != 9):
            return None
    
        for i in range(9):
            if (len(grid[i]) != 9):
                return None
            for j in range(9):
                if (grid[i][j] < 0 or grid[i][j] > 9):
                    return None    
    except (TypeError): # Not a list of list of int (this is more OO-friendly than "type()")
        return None
    # Iterate on all cells
    for i in range(9):
        for j in range(9):
            # Take care of the special case
            if (grid[i][j] == 0):
                continue
            # Unicity in each lines check
            for k in range(j+1,9):
                if (grid[i][k] == grid[i][j]):
                    return False

            # Unicity in each columns check
            for k in range(i+1,9):
                if (grid[k][j] == grid[i][j]):
                    return False
                
            # Unicity in each subgrid check
            # Find in which of the (3,3) subgrids we are
            subgrid_i = int(math.floor(i/3))
            subgrid_j = int(math.floor(j/3))
            # Check every cell in this subgrid
            for i2 in range(subgrid_i*3, subgrid_i*3 + 3):
                for j2 in range(subgrid_j*3, subgrid_j*3+3):
                    if ((i != i2 and j != j2) and grid[i][j] == grid[i2][j2]):
                        return False
    return True

def find_empty_cell(grid):
    empty_cell = None
    for i in range(9):
        for j in range(9):
            if (grid[i][j] == 0):
                empty_cell = [i,j]
                break
        if (empty_cell != None):
            break
    return empty_cell

def solve_sudoku (grid):
    integrity = is_correct_grid(grid)
    if (not integrity): # False or None
        return integrity
    # Simple and brutal backtracking :-)
    return solve_backtrack(grid)

def solve_backtrack(grid):
    empty_cell = find_empty_cell(grid)

    if (empty_cell != None or not is_correct_grid(grid)):
        # Fill the empty cell with 1..9 and recursively solve the 9 new sudokus
        i,j = empty_cell[0], empty_cell[1]
        while (grid[i][j] <= 9):
            grid[i][j]+= 1
            if (not is_correct_grid(grid)):
                continue
            solve_backtrack(grid)
            if (find_empty_cell(grid) == None and is_correct_grid(grid)): # A lower call found a solution
                break
        if (grid[i][j] > 9): # Dead end. Must backtrack
            grid[i][j] = 0
            return
    assert (is_correct_grid(grid))
    return grid
