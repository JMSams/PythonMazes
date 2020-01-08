from random import randint
from grid import Grid
from cell import Cell
from clear import clear
from time import sleep

def Mazify(grid):
	pairs = []
	sets = []
	for row in range(grid.rowCount):
		for col in range(grid.colCount):
			set = Set(Base62(len(sets)), [grid[col, row]])
			sets.append(set)
			
			grid[col, row].set = set
			grid[col, row].content = set.id
			
			if grid[col, row].east != None:
				pairs.append((grid[col, row], grid[col, row].east))
			if grid[col, row].north != None:
				pairs.append((grid[col, row], grid[col, row].north))
	
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
	
	for row in range(grid.rowCount):
		for col in range(grid.colCount):
			grid[col, row].content = " "

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
