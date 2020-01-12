def printhelp():
	print("Usage: python main.py -a:algorithm -c:colCount -r:rowCount")
	print("\talgorithm:")
	print("\t\t0 - Random")
	print("\t\t1 - Binary Tree")
	print("\t\t2 - Sidewinder")
	print("\t\t3 - Recursive Backtracker")
	print("\t\t4 - Kruskal")
	print("\t\t5 - Prims")
ALGORITHM_COUNT = 5

colCount = 7
rowCount = 7
algorithm = 0

from sys import argv
for arg in argv:
	if arg.startswith("-a:"):
		try:
			algorithm = int(arg[3:])
		except ValueError as e:
			printhelp()
			exit()
	elif arg.startswith("-c:"):
		try:
			colCount = int(arg[3:])
		except ValueError as e:
			printhelp()
			exit()
	elif arg.startswith("-r:"):
		try:
			rowCount = int(arg[3:])
		except ValueError as e:
			printhelp()
			exit()

from clear import clear
clear()

from random import randint
from grid import Grid

if algorithm == 0:
	algorithm = randint(1, ALGORITHM_COUNT)
if algorithm == 1:
	from BinaryTree import Mazify
elif algorithm == 2:
	from Sidewinder import Mazify
elif algorithm == 3:
	from RecursiveBacktracker import Mazify
elif algorithm == 4:
	from Kruskal import Mazify
elif algorithm == 5:
	from Prims import Mazify

grid = Grid(colCount, rowCount)
Mazify(grid)
#print(grid)

#TODO: Use threading to show an animation in the terminal while generating image
#TODO: Display the time taken for generating the maze and generating the image

from Image import OutputImage
OutputImage(grid)