import math
import random
import copy
from sudoku_solver_functions import *

number_of_random_iter = 100
number_of_fuzzed_iter = 10
FUZZRATIO = 0.05

def generate_random_grid():
	grid = []
	for i in range(9):
		grid.append([])
		for j in range(9):
			grid[i].append(random.randint(0, 9))

def fuzz_grid(grid, fuzzRatio=FUZZRATIO):
	fuzzNumber = random.randint(1, math.ceil(9 * 9 * fuzzRatio))
	print fuzzNumber
	for i in range(fuzzNumber):
		randX, randY = random.randint(0, 8), random.randint(0, 8)
		randValue = random.randint(0, 9)
		grid[randX][randY] = randValue

# Completely random input
illFormedRandomCount = 0
for i in range(number_of_random_iter):
	g = generate_random_grid()
	result = solve_sudoku(g)
	if (result == False or result == None):
		illFormedRandomCount += 1
	else:
		assert (is_correct_grid(g))
print "Random : Ended with " + str(illFormedRandomCount) + " ill-formed grids (for " + str(number_of_random_iter) + " tries)"

# Fuzzed input
grids = []
grids.append(easy)
grids.append(hard)

illFormedFuzzedCount = 0
for i in range(number_of_fuzzed_iter):
	selected_grid_number = random.randint(0, len(grids) - 1)
	g = copy.deepcopy(grids[selected_grid_number])
	fuzz_grid(g)
	result = solve_sudoku(g)
	if (result == False or result == None):
		illFormedFuzzedCount += 1
	else:
		assert (is_correct_grid(g))
print "Fuzzed : Ended with " + str(illFormedFuzzedCount) + " ill-formed grids (for " + str(number_of_fuzzed_iter) + " tries)"
