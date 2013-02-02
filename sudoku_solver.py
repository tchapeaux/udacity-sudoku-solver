from sudoku_solver_functions import *
import sys

if (__name__ == "__main__"):
    import copy
    import time

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
        print "No file given. Default grid used."
        grids.append(ill_formed)
        grids.append(valid)
        grids.append(invalid)
        grids.append(easy)
        print("default grid 'hard' was ignored")
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
            print "SOLUTION :\n" + grid_as_string(g_copy)
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
