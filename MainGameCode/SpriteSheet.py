import pygame as pg

class SpriteSheet:

    def __init__(self, filename, columns, rows):

        self.sheet = pg.image.load(filename)

        self.columns = columns
        self.rows = rows
        self.totalCellCount = columns * rows

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width / columns
        h = self.cellHeight = self.rect.height / rows
        hw, hh = self.cellCenter = (w/2, h/2)

        self.cells = list([(index % columns*w, index / columns * h, w, h) for index in range(self.totalCellCount)])
        self.handle = list([
            (0,0),(-hw,0),(-w,0),
            (0,-hh),(-hw,-hh),(-w,-hh),
            (0,-h),(-hw,-h),(-w,-h)])

    def draw(self, surface, cellIndex, x, y, handle=0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])
            
        
