import pygame as pg
from Settings import *

class Rules:
    def __init__(self):
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        rules = pg.image.load('../pictures/RulesPage.png')
        screen.blit(pg.transform.scale(rules, (WIDTH, HEIGHT)), [0, 0])
        pg.display.update()
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False
                    if event.key == pg.K_ESCAPE:
                        running = False
                        

    def show_start_screen(self):
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        rules = pg.image.load('../pictures/RulesPage.png')
        screen.blit(pg.transform.scale(rules, (WIDTH, HEIGHT)), [0, 0])
        pg.display.update()
        pass
