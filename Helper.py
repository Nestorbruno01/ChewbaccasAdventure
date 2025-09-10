import sys

import pygame
import random
import math
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
        self.pos_x = random.randint(1000, 1200)
        self.pos_y = random.randint(0, 700)
        self.speed = 2

    def animate(self):
        self.pos_x -= self.speed

    def draw(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))

class Bullet:
    def __init__(self, x, y):
        img = pygame.image.load('Media/Bullet.png')
        self.img = pygame.transform.scale(img, (20, 20))
        self.pos_x = x + 90
        self.pos_y = y + 35
        self.speed = 5

    def animate(self):
        self.pos_x += self.speed

    def draw(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))

def isCollided(Bullet, Stormtrooper):
    #finding the center coordinates
    bx = Bullet.pos_x + Bullet.img.get_width()  / 2
    by = Bullet.pos_y + Bullet.img.get_height() / 2
    tx = Stormtrooper.pos_x + Stormtrooper.img.get_width()  / 2
    ty = Stormtrooper.pos_y + Stormtrooper.img.get_height() / 2

    distance = math.sqrt(math.pow(bx - tx, 2) + math.pow(by - ty, 2))

    if distance < 60:
        return True
    else:
        return False

def draw_score(screen, text, x, y, color=(255, 255, 255), size=28, font_name=None):
    base_font = pygame.font.SysFont("Courier New", 48, bold=True)
    surface = base_font.render(text, True, color)
    screen.blit(surface, (x,y))

def Game_over(screen):
    img = pygame.image.load('Media/game_over.png')

    sw, sh = screen.get_size()
    iw, ih = img.get_size()
    rect = img.get_rect(center = (sw / 2, sh / 2))

    frozen = screen.copy()
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Courier New", 28, bold=True)
    prompt = font.render("SPACE : RESTART | Q: QUIT", True, (255, 255, 255))
    prompt_rect = prompt.get_rect(midtop=(sw / 2, rect.bottom + 16))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit(0)
                if event.key == pygame.K_SPACE:
                    return True


        screen.blit(frozen, (0, 0))
        screen.blit(img, rect)
        screen.blit(prompt, prompt_rect)
        pygame.display.flip()
        clock.tick(60)

def start_screen(screen):
    clock = pygame.time.Clock()
    sw, sh = screen.get_size()

    logo_img = pygame.image.load('Media/logo.png')
    logo_img = pygame.transform.scale(logo_img, (500, 500))
    logo_rect = logo_img.get_rect(center = (sw / 2, sh / 2))

    prompt_font = pygame.font.SysFont("Courier New", 28, bold=True)
    prompt = prompt_font.render("Press SPACE to start", False, (200, 200, 200))
    prompt_rect = prompt.get_rect(midtop = (sw // 2, sh // 2 + 180))

    controls_font = pygame.font.SysFont("Courier New", 20, bold=True)
    controls = controls_font.render("Move: UP and DOWN | Shoot: SPACE", False, (200, 200, 200))
    controls_rect = controls.get_rect(center = (sw // 2, sh // 2 + 260))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
        screen.fill((0, 0, 0))
        screen.blit(logo_img, logo_rect)
        screen.blit(prompt, prompt_rect)
        screen.blit(controls, controls_rect)
        pygame.display.flip()
        clock.tick(60)











