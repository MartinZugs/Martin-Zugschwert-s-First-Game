from Settings import *
import pygame as pg
from pygame.locals import *
import sys

pg.init()
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption(TITLE)
pg.key.set_repeat(100, 0)

CCM = MAIN_MALE_CHARACTER_WALKING_DOWN

CENTER_HANDLE = 4

UIndex = 0
DIndex = 0
RIndex = 0
LIndex = 0
x = 0
y = 0
currentIndex = DIndex

def events():

    global CCM
    global UIndex
    global DIndex
    global RIndex
    global LIndex
    global currentIndex
    global x
    global y


    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pg.quit()
                sys.exit()
            elif event.key == K_w:
                CCM = MAIN_MALE_CHARACTER_WALKING_UP
                UIndex += 1
                currentIndex = UIndex
                y = y + 5
            elif event.key == K_a:
                CCM = MAIN_MALE_CHARACTER_WALKING_LEFT
                LIndex += 1
                currentIndex = LIndex
                x = x + 5
            elif event.key == K_s:
                CCM = MAIN_MALE_CHARACTER_WALKING_DOWN
                DIndex += 1
                currentIndex = DIndex
                y = y - 5
            elif event.key == K_d:
                CCM = MAIN_MALE_CHARACTER_WALKING_RIGHT
                RIndex += 1
                currentIndex = RIndex
                x = x - 5
        else:
            reset_index()


def reset_index():
     
    global UIndex
    global DIndex
    global RIndex
    global LIndex
    global currentIndex
    UIndex = 0
    DIndex = 0
    RIndex = 0
    LIndex = 0
    currentIndex = DIndex

while True:

    screen.fill(BLACK)
    screen.blit(pwoods, (x,y))

    CCM.draw(screen, currentIndex % CCM.totalCellCount, HW, HH, CENTER_HANDLE)

    events()
        
    pg.display.update()
    CLOCK.tick(FPS)
    
