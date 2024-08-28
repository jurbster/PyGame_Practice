#Game to practice and learn PyGame

import pygame

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#Variable that keeps the main loop running
running = True


#Main loop
while running:

    for event in pygame.event.get():
        #Did the user hit a key?
        if event.type == KEYDOWN:
            #Stop loop if it was the Escape key
            if event.key == K_ESCAPE:
                running = False
        #Stop loop if user hits close button
        elif event.type == QUIT:
            running = False

    #Fill screen with white
    screen.fill((255, 255, 255))

    #Create a surface and pass in length and width
    surf = pygame.Surface((50, 50))

    #Give the surface a color
    surf.fill((0, 0, 0))
    rect = surf.get_rect()

    #Put the center of the surace at the center of the screen display
    surf_center = (
        (SCREEN_WIDTH-surf.get_width())/2,
        (SCREEN_HEIGHT-surf.get_width())/2
    )

    #Draw the surface to the screen
    screen.blit(surf, surf_center)
    pygame.display.flip()

