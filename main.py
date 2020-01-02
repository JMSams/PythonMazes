import sys

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

if (len(sys.argv) > 1):
	if (sys.argv[1] == 'BinaryTree'):
		from BinaryTree import BinaryTree as Algorithm
	#elif (sys.argv[1] == 'RecursiveBacktracker'):
		#import RecursiveBacktracker.RecursiveBacktracker as Algorithm
	else:
		from BinaryTree import BinaryTree as Algorithm
else:
	from BinaryTree import BinaryTree as Algorithm

themaze = Algorithm(randint(3, 12), randint(3, 12))
print("rows: " + str(themaze.rows))
print("cols: " + str(themaze.columns))
print(themaze)
exit()
for row in range(themaze.rows):
	for col in range(themaze.columns):
		print("({},{}): [{}]".format(col, row,  ", ".join(map(str, themaze.data[row][col].links))))