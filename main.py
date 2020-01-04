import colorama
colorama.init()

from os import system, name
def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')
clear()

from random import randint

from options import *

if ALGORITHM == 0 or ALGORITHM < 0 or ALGORITHM > ALGORITHM_COUNT:
	ALGORITHM = randint(1, ALGORITHM_COUNT)
if ALGORITHM == 1:
	from BinaryTree import BinaryTree as Algorithm
	AlgorithmName = "Binary Tree"
elif ALGORITHM == 2:
	from RecursiveBacktracker import RecursiveBacktracker as Algorithm
	AlgorithmName = "Recursive Backtracker"
elif ALGORITHM == 3:
	from Sidewinder import Sidewinder as Algorithm
	AlgorithmName = "Sidewinder"

rows = GRID_SIZE_Y if isinstance(GRID_SIZE_Y, int) else randint(GRID_SIZE_Y[0], GRID_SIZE_Y[1])
cols = GRID_SIZE_X if isinstance(GRID_SIZE_X, int) else randint(GRID_SIZE_X[0], GRID_SIZE_X[1])
themaze = Algorithm(rows, cols)

print("Algorithm: " + AlgorithmName)
print(themaze)