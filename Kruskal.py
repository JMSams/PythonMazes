from random import randint
from maze import Maze
from cell import Cell
from clear import clear
from time import sleep

def Kruskal(rows, cols):
	maze = Maze(rows, cols)
	
	pairs = []
	sets = []
	for row in range(rows):
		for col in range(cols):
			set = Set(Base62(len(sets)), [maze.data[row][col]])
			sets.append(set)
			
			maze.data[row][col].set = set
			maze.data[row][col].content = set.id
			
			if maze.data[row][col].east != None:
				pairs.append((maze.data[row][col], maze.data[row][col].east))
			if maze.data[row][col].north != None:
				pairs.append((maze.data[row][col], maze.data[row][col].north))
	
	while len(sets) > 1:
		pair = pairs.pop(randint(0, len(pairs)-1))
		if pair[0].set == pair[1].set:
			continue
		
		pair[0].Link(pair[1])
		if len(pair[0].set) >= len(pair[1].set):
			other = pair[1].set
			pair[0].set.Combine(other)
			sets.remove(other)
		else:
			other = pair[0].set
			pair[1].set.Combine(other)
			sets.remove(other)
	
	for row in range(rows):
		for col in range(cols):
			maze.data[row][col].content = " "
	
	return maze

class Set(list):
	id = ""
	
	def __init__(self, id, cells=[]):
		super().__init__()
		self.id = id
		for cell in cells:
			self.append(cell)
	
	def Combine(self, other):
		for cell in other:
			self.append(cell)
			cell.set = self
			cell.content = self.id

def Base62(num):
	BASE62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	if num == 0:
		return BASE62[0]
	arr = []
	while num:
		num, rem = divmod(num, 62)
		arr.append(BASE62[rem])
	arr.reverse()
	return ''.join(arr)
