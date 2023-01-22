import pygame
from character import *
from settings import *
import os

class Charlie(Character):
    charlie_img = pygame.image.load('../big_team/characters/charlie.png').convert_alpha()
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.x, self.y = player_pos
        self.character_img = charlie_img
        self.max_health = health

    def draw(self, WIN):
        super().draw(WIN)
        self.healthbar(WIN)
