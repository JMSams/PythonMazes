from grid import Grid
from cubeCell import CubeCell

class CubeGrid(Grid):
	cubeSize = -1
	
	def __init__(self, cubeSize):
		self.cubeSize = cubeSize
		super().__init__(cubeSize, cubeSize)
	
	def eachCell(self):
		for face in range(6):
			for col in range(self.colCount):
				for row in range(self.rowCount):
					yield self[face, col, row]
	
	def eachRow(self):
		for face in range(6):
			for row in range(self.rowCount):
				rv = []
				for col in range(self.colCount):
					rv.append(self[face, col, row])
				yield rv
	
	def PrepareGrid(self):
		for face in range(6):
			newFace = []
			for col in range(self.colCount):
				newCol = []
				for row in range(self.rowCount):
					newCol.append(CubeCell(face, col, row))
				newFace.append(newCol)
			self.grid.append(newFace)
	
	def ConfigureGrid(self):
		for face in range(6):
			for col in range(self.colCount):
				for row in range(self.rowCount):
					self[face, col, row].north = self[face, col, row+1]
					self[face, col, row].south = self[face, col, row-1]
					self[face, col, row].east = self[face, col+1, row]
					self[face, col, row].west = self[face, col-1, row]
	
	def __getitem__(self, coord):
		face,col,row = coord
		
		if face < 0 or face >= 6:
			return None
		
		face,col,row = self.wrap(face, col, row)
		
		return self.grid[face][col][row]
	
	def wrap(self, face, col, row):
		n = self.cubeSize-1
		d = self.cubeSize
		
		if row < 0:
			if face == 0:   return (4, col, 0)
			elif face == 1: return (4, n, col)
			elif face == 2: return (4, n-col, n)
			elif face == 3: return (4, 0, n-col)
			elif face == 4: return (3, 0, n-col)
			elif face == 5: return (1, n, col)
		elif row >= d:
			if face == 0:   return (5, n-col, 0)
			elif face == 1: return (5, 0, col)
			elif face == 2: return (5, col, n)
			elif face == 3: return (5, n, n-col)
			elif face == 4: return (1, 0, col)
			elif face == 5: return (3, n, n-col)
		elif col < 0:
			if face == 0:   return (3, row, n)
			elif face == 1: return (0, row, n)
			elif face == 2: return (1, row, n)
			elif face == 3: return (2, row, n)
			elif face == 4: return (0, 0, row)
			elif face == 5: return (0, n, n-row)
		elif col >= d:
			if face == 0:   return (1, row, 0)
			elif face == 1: return (2, row, 0)
			elif face == 2: return (3, row, 0)
			elif face == 3: return (0, row, 0)
			elif face == 4: return (2, 0, n-row)
			elif face == 5: return (2, n, row)
		else:
			return (face, col, row)
	
	def randomCell(self):
		return self[randint(0, 5), randint(0, self.colCount-1), randint(0, self.rowCount-1)]
	
	def __str__(self):
		pass
		#TODO: Somehow represent a cube maze as text?
	
	def Draw(self, outputName="output"):
		from PIL import Image
		import Sprites
		
		#TODO: Draw the net of the cube grid