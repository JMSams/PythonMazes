def printhelp():
	print("Usage: python main.py -a:algorithm -c:colCount -r:rowCount")
	print("\t-a --algorithm")
	print("\t\t0 - Random")
	print("\t\t1 - Binary Tree")
	print("\t\t2 - Sidewinder")
	print("\t\t3 - Recursive Backtracker")
	print("\t\t4 - Kruskal")
	print("\t\t5 - Prims")
	print("\t-t --terminal")
	print("\t\tIf set, maze will be printed to stdout")
	print("\t-m --mazetype")
	print("\t\t1: Generates a rectangular maze.")
	print("\t\t2: Generates a cubic maze.")
	exit()
ALGORITHM_COUNT = 5

colCount = 7
rowCount = 7
algorithm = 0
printmaze = False
outname = "output"

mazeType = 1
mazeTypes = 2

from sys import argv
for arg in argv:
	if arg.startswith("-a:"):
		try:
			algorithm = int(arg[3:])
		except ValueError as e:
			printhelp()
	elif arg.startswith("-c:"):
		try:
			colCount = int(arg[3:])
		except ValueError as e:
			printhelp()
	elif arg.startswith("-r:"):
		try:
			rowCount = int(arg[3:])
		except ValueError as e:
			printhelp()
	elif arg == "-h":
		printhelp()
	elif arg == "-t":
		if mazeType != 2:
			printmaze = True
	elif arg.startswith("-o:"):
		outname = arg[3:]
	elif arg.startswith("-m:"):
		try:
			mt = int(arg[3:])
			if mt >= 1 and mt <= mazeTypes:
				mazeType = mt
			else:
				printhelp()
		except ValueError as e:
			printhelp()

from clear import clear
clear()

from random import randint
from threading import Thread
from datetime import datetime
from time import sleep

def Animate(s, t=None):
	if t == None:
		i = 0
		while runt:
			print("\033[F\033[K{}{}".format(s, ((i%3)+1)*'.'))
			i+=1
			sleep(0.1)
	else:
		i = 0
		while t==None or t.is_alive():
			print("\033[F\033[K{}{}".format(s, ((i%3)+1)*'.'))
			i+=1
			sleep(0.1)

if algorithm == 0:
	algorithm = randint(1, ALGORITHM_COUNT)
if algorithm == 1:
	from BinaryTree import Mazify
	algorithm = "Binary Tree"
elif algorithm == 2:
	from Sidewinder import Mazify
	algorithm = "Sidewinder"
elif algorithm == 3:
	from RecursiveBacktracker import Mazify
	algorithm = "Recursive Backtracker"
elif algorithm == 4:
	from Kruskal import Mazify
	algorithm = "Kruskal"
elif algorithm == 5:
	from Prims import Mazify
	algorithm = "Prims"

if mazeType == 1:
	from grid import Grid
elif mazeType == 2:
	from cubeGrid import CubeGrid as Grid
else:
	printhelp()

gridtime = datetime.now()
grid = Grid(colCount, rowCount)
runt = True
t = Thread(target=Animate, args=("Generating maze with "+algorithm,))
t.daemon = True
t.start()
Mazify(grid)
runt = False
if printmaze:
	print(grid)
print("Maze generated in {0:.2f} seconds".format((datetime.now()-gridtime).total_seconds()))
print()

imagetime = datetime.now()
t = Thread(target=grid.Draw, args=(outname,))
t.daemon = True
t.start()
Animate("Generating image", t)

print("Image generated in {0:.2f} seconds, saved as  {1}.png".format((datetime.now()-imagetime).total_seconds(), outname))