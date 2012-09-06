import math
import random
from sudoku_solver_functions import *
number_of_iter = 10000

def generate_random_grid():
	grid = []
	for i in range(9):
		grid.append([])
		for j in range(9):
			grid[i].append(random.randint(0,9))

incorrectCount = 0
for i in range(number_of_iter):
	g = generate_random_grid()
	result = solve_sudoku(g)
	if (result == False or result == None):
		incorrectCount += 1
	else:
		assert (is_correct_grid(g))

print "Ended with " + str(incorrectCount) + " ill-formed grids"
