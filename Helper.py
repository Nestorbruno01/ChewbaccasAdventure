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

    def animate(self):
        moving_up = False
        moving_down = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    moving_up = True
                    moving_down = False
                    self.pos_y -= 10
                elif event.key == pygame.K_DOWN:
                    moving_up = False
                    moving_down = True
                    self.pos_y += 10
            elif event.type == pygame.KEYUP:
                moving_up = False
                moving_down = False



    def draw(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))

class StormTrooper:
    def __init__(self):
        img = pygame.image.load('Media/storm_trooper.png')
        img = pygame.transform.scale(img, (100, 100))
        self.img = pygame.transform.flip(img, True, False)
        self.pos_x = random.randint(800, 1000)
        self.pos_y = random.randint(0, 1000)

    def draw(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))





