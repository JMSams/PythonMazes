from cell import Cell

class CubeCell(Cell):
	face = None
	
	def __init__(self, grid, face, col, row):
		self.face = face
		super().__init__(grid, col, row)