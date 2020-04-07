from random import randint
from random import choice
from cell import Cell

class Grid:
    colCount = -1
    rowCount = -1
    
    grid = None
    
    def __init__(self, colCount, rowCount):
        self.colCount = colCount
        self.rowCount = rowCount
        
        self.grid = []
        self.PrepareGrid()
        self.ConfigureGrid()
    
    def cellCount(self):
        return self.colCount * self.rowCount
    
    def eachCell(self):
        for col in range(self.colCount):
            for row in range(self.rowCount):
                yield self[col, row]
    
    def eachRow(self):
        for row in range(self.rowCount):
            rv = []
            for col in range(self.colCount):
                rv.append(self[col, row])
            yield rv
    
    def PrepareGrid(self):
        for col in range(self.colCount):
            newCol = []
            for row in range(self.rowCount):
                newCol.append(Cell(self, col, row))
            self.grid.append(newCol)
    
    def ConfigureGrid(self):
        for cell in self.eachCell():
            cell.north = self[cell.col, cell.row+1]
            cell.south = self[cell.col, cell.row-1]
            cell.east = self[cell.col+1, cell.row]
            cell.west = self[cell.col-1, cell.row]
    
    def __getitem__(self, coord):
        col,row = coord
        if col < 0:
            return None
        elif col >= self.colCount:
            return None
        elif row < 0:
            return None
        elif row >= self.rowCount:
            return None
        else:
            return self.grid[col][row]
    
    def orphans(self):
        rv = []
        for cell in self.eachCell():
            if len(cell.links) == 0:
                rv.append(cell)
        return rv
    
    def deadends(self):
        rv = []
        for cell in self.eachCell():
            if len(cell.links) == 1:
                rv.append(cell)
        return rv
    
    def randomCell(self):
        return self[randint(0, self.colCount-1), randint(0, self.rowCount-1)]
    
    def randomDeadend(self):
        return choice(self.deadends())
    
    def __str__(self):
        rv = ""
        
        rv += "+"
        for col in range(self.colCount):
            rv += "---+"
        rv += "\n"

        for row in range(self.rowCount-1, -1, -1):
            rv += "|"
            for col in range(self.colCount):
                rv += " " + self[col,row].content + " "
                if col == self.colCount-1:
                    rv += "|"
                else:
                  rv += " " if self[col, row].east in self[col, row].links else "|"
            rv += "\n"
            
            rv += "+"
            for col in range(self.colCount):
                rv += "   +" if self[col, row].south in self[col, row].links else "---+"
            rv += "\n"
        
        return rv
    
    def Draw(self, outputName="output"):
        from PIL import Image
        import Sprites
        
        image_width = self.colCount * Sprites.CellSize
        image_height = self.rowCount * Sprites.CellSize
        
        image = Image.new('RGBA', (image_width, image_height), 'black')
        
        for row in range(self.rowCount):
            for col in range(self.colCount):
                offset = ((col * Sprites.CellSize), (image_height - ((row+1) * Sprites.CellSize)))
                
                sprite = Sprites.SelectSprite(self[col, row])
                image.paste(sprite, offset)
        
        image.save(outputName + ".png")