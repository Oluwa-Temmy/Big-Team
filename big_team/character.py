import pygame as pg
from settings import *

class Character:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.character_img = None

    def draw(self,WIN):
        WIN.blit(self.charcater_img, (self.x, self.y))

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            player.y -= player_vel
        if keys[pg.K_s]:
            player.y += player_vel
        if keys [pg.K_d]:
            player.x += player_vel
        if keys[pg.K_a]:
            player.x -= player_vel

    def healthbar(self,WIN):
        pygame.draw.rect(WIN, (255,0,0), (self.x, self.y + self.character_img.get_height() + 10, 10, self.character_img.get_width()))
        pygame.draw.rect(WIN, (0,0,139), (self.x, self.y + self.character_img.get_height() + 10, 10,  self.character_img.get_width() * (self.health/self.max_health)))

    def update(self):
        self.movement()

    def get_width(self):
        return self.character_img.get_width()

    def get_height(self):
        return self.character_img.get_height()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
