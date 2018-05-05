from Settings import *
import pygame as pg
from pygame.locals import *
import sys

pg.init()
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption(TITLE)
pg.key.set_repeat(100,100)

CCM = MAIN_MALE_CHARACTER_WALKING_DOWN

CENTER_HANDLE = 4

UIndex = 0
DIndex = 0
RIndex = 0
LIndex = 0
currentIndex = DIndex

def events():

    global Index
    global CCM
    global UIndex
    global DIndex
    global RIndex
    global LIndex
    global currentIndex
    global screen
    running = True

    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pg.quit()
                sys.exit()
            elif event.key == K_w:
                CCM = MAIN_MALE_CHARACTER_WALKING_UP
                UIndex += 1
                currentIndex = UIndex
            elif event.key == K_a:
                CCM = MAIN_MALE_CHARACTER_WALKING_LEFT
                LIndex += 1
                currentIndex = LIndex
            elif event.key == K_s:
                CCM = MAIN_MALE_CHARACTER_WALKING_DOWN
                DIndex += 1
                currentIndex = DIndex
            elif event.key == K_d:
                CCM = MAIN_MALE_CHARACTER_WALKING_RIGHT
                RIndex += 1
                currentIndex = RIndex


def get_current_index():
    return currentIndex

while True:

    #currentIndex = 0

    screen.fill(BLACK)

    CCM.draw(screen, get_current_index() % CCM.totalCellCount, HW, HH, CENTER_HANDLE)

    events()
        
    pg.display.update()
    CLOCK.tick(FPS)
    
