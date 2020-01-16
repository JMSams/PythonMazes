from random import randint

class Kruskal:
	name = "Kruskal"
	supportedGrids = [1, 2]
	
	@staticmethod
	def On(grid):
		pairs = []
		sets = []
		
		for cell in grid.eachCell():
			set = Kruskal.Set([cell])
			cell.set = set
			sets.append(set)
			
			if cell.north != None:
				pairs.append((cell, cell.north))
			if cell.east != None:
				pairs.append((cell, cell.east))
		
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