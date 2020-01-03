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

if ALGORITHM == 0:
	ALGORITHM = randint(1, 2)
if ALGORITHM == 1:
	from BinaryTree import BinaryTree as Algorithm
elif ALGORITHM == 2:
	from RecursiveBacktracker import RecursiveBacktracker as Algorithm

themaze = Algorithm(randint(3, 12), randint(3, 12))
print("rows: " + str(themaze.rows))
print("cols: " + str(themaze.columns))
print(themaze)