import pygame
import random

from Helper import Chewbacca, StormTrooper, Bullet, isCollided

# Background Screen
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 1100
BACKGROUND_img = pygame.image.load('Media/Background.png')
BACKGROUND_img = pygame.transform.scale(BACKGROUND_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

#start the library
pygame.init()

#draw the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

chewbacca = Chewbacca()
stormtrooper = StormTrooper()

cooldown = 0

# Init the clock
clock = pygame.time.Clock()

bullets = []
stormtroops = []

# Timing the spawns in frames
SPAWN_min = 90
SPAWN_max = 150
spawn_timer = random.randint(SPAWN_min, SPAWN_max)

flag = True
while flag:
    # ticking the clock
    clock.tick(60)

    # drawing the background
    screen.blit(BACKGROUND_img, (0, 0))
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if cooldown == 0:
                #spawning a bullet at Chewbaccas position
                bullets.append(Bullet(chewbacca.pos_x, chewbacca.pos_y))
                cooldown = 15

    spawn_timer -= 1
    if spawn_timer < 0:
        stormtroops.append(StormTrooper())
        spawn_timer = random.randint(SPAWN_min, SPAWN_max)

    # Using blit to copy image to screen at a specific location
    chewbacca.draw(screen)
    chewbacca.animate()

    for b in bullets[:]:
        b.draw(screen)
        b.animate()
        if b.pos_x > SCREEN_WIDTH:
            bullets.remove(b)

    for st in stormtroops:
        st.draw(screen)
        st.animate()

    for b in bullets:
        for st in stormtroops:
            if isCollided(b, st):
                bullets.remove(b)
                stormtroops.remove(st)
                break

    if cooldown > 0:
        cooldown -= 1

    # refresh the display
    pygame.display.flip()



pygame.quit()
exit(0)