import pygame as pg
import sys
from settings import *
from charlie import *
from map import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(WIN)
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.charlie = Charlie(self)
        self.map = Map(self)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        self.charlie.update()

    def draw(self):
        self.screen.fill('black')
        self.charlie.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                exit()

    def run(self):
        while RUN:
            self.check_events()
            self.draw()
            self.update()


if __name__ == '__main__':
    game = GAME()
    game = game.run()
