import pygame
import random
from IPython.core.completer import position_to_cursor
from IPython.core.events import post_execute


class Chewbacca:
    def __init__(self):
        img = pygame.image.load('Media/chewbacca.png')
        self.img = pygame.transform.scale(img, (100, 100))
        #Character position
        self.pos_x = 100
        self.pos_y = 600
        self.speed = 4

    def animate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.pos_y -= self.speed
        if keys[pygame.K_DOWN]:
            self.pos_y += self.speed




    def draw(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))

class StormTrooper:
    def __init__(self):
        img = pygame.image.load('Media/storm_trooper.png')
        img = pygame.transform.scale(img, (100, 100))
        self.img = pygame.transform.flip(img, True, False)
        self.pos_x = random.randint(800, 1000)
        self.pos_y = random.randint(0, 1000)
        self.speed = 2

    def animate(self):
        self.pos_x -= self.speed

    def draw(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))





