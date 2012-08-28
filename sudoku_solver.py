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

def solve_sudoku (grid):
    integrity = is_correct_grid(grid)
    if (not integrity): # False or None
        return integrity
    # Simple and brutal backtracking :-)
    solve_backtrack(grid, [])
    
def solve_backtrack(grid, solution):
    #print grid
    # Find an empty cell
    empty_cell = None
    for i in range(9):
        for j in range(9):
            if (grid[i][j] == 0):
                empty_cell = [i,j]
                break
        if (empty_cell != None):
            break
    
    # If no empty cell were found and grid is still correct, we have the solution
    if (empty_cell == None and is_correct_grid(grid)):
        for i in range(9):
            solution.append(grid[i])
    else:
        # Fill the empty cell with 1..9 and recursively solve the 9 new sudokus
        i,j = empty_cell[0], empty_cell[1]
        while (grid[i][j] <= 9):
            grid[i][j]+= 1
            if (not is_correct_grid(grid)):
                continue
            solve_backtrack(grid, solution)
            if (solution != []): # A lower call found a solution
                break
        if (grid[i][j] > 9): # Dead end. Must backtrack
            grid[i][j] = 0
            return
    if (solution == []):
        raise Exception("Unsolvable Grid")
    return solution

import copy
import time

grids = [ill_formed, valid, invalid, easy, hard]

for g in grids:
    if (is_correct_grid(g)):
        g_copy = copy.deepcopy(g)
	start_time = time.time()        
	solve_sudoku(g_copy)
	stop_time = time.time()
        assert (is_correct_grid(g_copy))
        for i in range(9):
            for j in range(9):
                assert (g_copy[i][j] != 0)
                assert g[i][j] == 0 or g[i][j] == g_copy[i][j]
	print "found solution in ", stop_time - start_time, " second(s) :"
	print g_copy

