from cell import Cell

class CubeCell(Cell):
	face = None
	
	def __init__(self, face, col, row):
		self.face = face
		super().__init__(col, row)