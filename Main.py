import pygame

from Helper import Chewbacca, StormTrooper

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

# Init the clock
clock = pygame.time.Clock()

flag = True
while flag:
    # ticking the clock
    clock.tick(60)

    # drawing the background
    screen.blit(BACKGROUND_img, (0, 0))
    # Using blit to copy image to screen at a specific location
    chewbacca.draw(screen)
    stormtrooper.draw(screen)


    chewbacca.animate()
    stormtrooper.animate()
    # refresh the display
    pygame.display.flip()

    # code you need to end pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

pygame.quit()
exit(0)