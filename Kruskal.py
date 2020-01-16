from random import randint
from grid import Grid
from cell import Cell
from clear import clear
from time import sleep

class Kruskal:
	name = "Kruskal"
	supportedGrids = [1, 2]
	
	@staticmethod
	def On(grid):
		if isinstance(grid, CubeGrid):
			Kruskal.MazifyCubed(grid)
		else:
			Kruskal.Mazify(grid)
	
	@staticmethod
	def Mazify(grid):
		pairs = []
		sets = []
		for row in range(grid.rowCount):
			for col in range(grid.colCount):
				set = Set([grid[col, row]])
				sets.append(set)
				
				grid[col, row].set = set
				
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
	
	@staticmethod
	def MazifyCubed(grid):
		pairs = []
		sets = []
		for face in range(6):
			for row in range(grid.rowCount):
				for col in range(grid.colCount):
					set = Set([grid[face, col, row]])
					sets.append(set)
					
					grid[face, col, row].set = set
					
					if grid[face, col, row].east != None:
						pairs.append((grid[face, col, row], grid[face, col, row].east))
					if grid[face, col, row].north != None:
						pairs.append((grid[face, col, row], grid[face, col, row].north))
		
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
	
	class Set(list):
		def __init__(self, cells=[]):
			super().__init__()
			for cell in cells:
				self.append(cell)
		
		def Combine(self, other):
			for cell in other:
				self.append(cell)
				cell.set = self
	
	@staticmethod
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