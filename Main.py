import pygame
import random

from Helper import Chewbacca, StormTrooper, Bullet, isCollided, draw_score, Game_over, start_screen

# Background Screen
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800
BACKGROUND_img = pygame.image.load('Media/Background.png')
BACKGROUND_img = pygame.transform.scale(BACKGROUND_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

#start the library
pygame.init()

#draw the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

start_screen(screen)

chewbacca = Chewbacca()

cooldown = 0

# Init the clock
clock = pygame.time.Clock()

bullets = []
stormtroops = []

# Timing the spawns in frames
SPAWN_min = 90
SPAWN_max = 150
spawn_timer = random.randint(SPAWN_min, SPAWN_max)

score = 0

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
        # bullet shooting, when pressing SPACE
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if cooldown == 0:
                #spawning a bullet at Chewbaccas position
                bullets.append(Bullet(chewbacca.pos_x, chewbacca.pos_y))
                cooldown = 25
    # Bullet cooldown
    if cooldown > 0:
        cooldown -= 1

    # spawning the stormtroops
    spawn_timer -= 1
    if spawn_timer < 0:
        stormtroops.append(StormTrooper())
        spawn_timer = random.randint(SPAWN_min, SPAWN_max)

    # Using blit to copy image to screen at a specific location
    chewbacca.draw(screen)
    chewbacca.animate()

    # animating the bullets.
    for b in bullets[:]:
        b.draw(screen)
        b.animate()
        if b.pos_x > SCREEN_WIDTH:
            bullets.remove(b)

    # animating the troops
    for st in stormtroops:
        st.draw(screen)
        st.animate()

        #Game over if Stormtrooper gets past
        if st.pos_x + st.img.get_width() < chewbacca.pos_x:
            if Game_over(screen):
                chewbacca = Chewbacca()
                cooldown = 0
                bullets.clear()
                stormtroops.clear()
                spawn_timer = random.randint(SPAWN_min, SPAWN_max)
                break
            else:
                flag = False
                break

    #Collision detection
    for b in bullets:
        for st in stormtroops:
            if isCollided(b, st):
                bullets.remove(b)
                stormtroops.remove(st)
                score += 1
                break

    draw_score(screen, f"Score: {score}", 16, 16)


    # refresh the display
    pygame.display.flip()



pygame.quit()
exit(0)