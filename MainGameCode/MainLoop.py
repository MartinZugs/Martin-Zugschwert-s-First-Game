from Settings import *
import pygame as pg
from pygame.locals import *
import sys

def events():
    for event in pg.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pg.quit()
            sys.exit()

pg.init()
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption(TITLE)

CENTER_HANDLE = 4

Index = 0

while True:
    events()
    screen.fill(BLACK)
    MAIN_MALE_CHARACTER_WALKING_RIGHT.draw(screen, Index % MAIN_MALE_CHARACTER_WALKING_RIGHT.totalCellCount, HW, HH, CENTER_HANDLE)
    Index += 1

        
    pg.display.update()
    CLOCK.tick(FPS)
    
