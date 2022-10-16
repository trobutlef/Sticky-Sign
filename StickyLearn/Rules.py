import pygame as pg
from Settings import *

class Rules:
    def __init__(self):
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Practice Mode')
        screen.fill(LIGHTPINK)
        pg.display.update()
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False
                        

    def show_start_screen(self):
        screen = pg.display.set_mode((700, 700))
        pg.display.set_caption('StickySign Rules')
        screen.fill(LIGHTPINK)
        pg.display.update()
        pass
