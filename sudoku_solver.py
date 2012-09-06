from define_grids import *
import math
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

import copy
import time
import sys

grids = []
argc = len(sys.argv)
for i in range(1, argc):
    filename = sys.argv[1]
    try:
        f = open(filename)
        grids.append(parse_string(f.read()))
        f.close()
    except IOError:
        print "Opening of " + filename + " failed."

if (argc == 1):
    grids.append(ill_formed)
    grids.append(valid)
    grids.append(invalid)
    grids.append(easy)
    #grids.append(hard)

for g in grids:
    print "GRID : \n" + grid_as_string(g)
    if (is_correct_grid(g)):
        g_copy = copy.deepcopy(g)
        start_time = time.time()
        solve_sudoku(g_copy)
        stop_time = time.time()
        for i in range(9):
            for j in range(9):
                assert (g_copy[i][j] != 0)
                assert g[i][j] == 0 or g[i][j] == g_copy[i][j]
        print "found solution in ", stop_time - start_time, " second(s) :"
        print "SOLUTION :\n"+ grid_as_string(g_copy)
    else:
        print "Not a correct grid! :("

# INITIAL INSTRUCTIONS

# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.
