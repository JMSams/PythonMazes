from random import randint
from grid import Grid
from cubeCell import CubeCell

class CubeGrid(Grid):
	cubeSize = -1
	
	def __init__(self, cubeSize):
		self.cubeSize = cubeSize
		super().__init__(cubeSize, cubeSize)
	
	def cellCount(self):
		return self.colCount * self.rowCount * 6
	
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
			if face == 0:   return (5, 0, col)
			elif face == 1: return (5, col, n)
			elif face == 2: return (5, n, col)
			elif face == 3: return (5, n-col, 0)
			elif face == 4: return (1, col, n)
			elif face == 5: return (3, n-col, 0)
		elif row >= d:
			if face == 0:   return (4, 0, n-col)
			elif face == 1: return (4, col, 0)
			elif face == 2: return (4, n, col)
			elif face == 3: return (4, n-col, n)
			elif face == 4: return (3, n-col, n)
			elif face == 5: return (1, col, 0)
		elif col < 0:
			if face == 0:   return (3, n, row)
			elif face == 1: return (0, n, row)
			elif face == 2: return (1, n, row)
			elif face == 3: return (2, n, row)
			elif face == 4: return (0, n-row, n)
			elif face == 5: return (0, row, 0)
		elif col >= d:
			if face == 0:   return (1, 0, row)
			elif face == 1: return (2, 0, row)
			elif face == 2: return (3, 0, row)
			elif face == 3: return (0, 0, row)
			elif face == 4: return (2, row, n)
			elif face == 5: return (2, n-row, 0)
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
		
		facesize = self.cubeSize * Sprites.CellSize
		
		faceOffsets = [
			(0, facesize),
			(facesize, facesize),
			(facesize*2, facesize),
			(facesize*3, facesize),
			(facesize, 0),
			(facesize, facesize*2)
		]
		
		image = Image.new('RGBA', (facesize*4, facesize*3), (0, 0, 0, 0))
		
		for face in range(6):
			for row in range(self.cubeSize):
				for col in range(self.cubeSize):
					offset = ((col * Sprites.CellSize), (facesize - ((row+1) * Sprites.CellSize)))
					offset = (offset[0] + faceOffsets[face][0], offset[1] + faceOffsets[face][1])
					
					sprite = Sprites.SelectSprite(self[face, col, row])
					image.paste(sprite, offset)
		
		image.save(outputName+".png")
		
		#debug
		with open(outputName+".log", "w") as f:
			f.write("Debug output\n\n")
			for cell in self.eachCell():
				f.write("Cell ({}, {}, {}):\n".format(cell.face, cell.col, cell.row))
				f.write("\tNorth {} ({}, {}, {})\n".format(" | " if cell.IsLinked(cell.north) else "<=>", cell.north.face, cell.north.col, cell.north.row))
				f.write("\tEast {} ({}, {}, {})\n".format(" | " if cell.IsLinked(cell.east) else "<=>", cell.east.face, cell.east.col, cell.east.row))
				f.write("\tSouth {} ({}, {}, {})\n".format(" | " if cell.IsLinked(cell.south) else "<=>", cell.south.face, cell.south.col, cell.south.row))
				f.write("\tWest {} ({}, {}, {})\n".format(" | " if cell.IsLinked(cell.west) else "<=>", cell.west.face, cell.west.col, cell.west.row))