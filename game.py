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

#Define a Player object - extending pygame.sprite.Sprite
#Surface drawn on screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    #Move the player based on user keys
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#Instantiate player
player = Player()

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

    #Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    #Update the player sprite based on user keypresses
    player.update(pressed_keys)

    #Give the surface a color
    screen.fill((0, 0, 0))

    screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    #Put the center of the surace at the center of the screen display
    #surf_center = (
        #(SCREEN_WIDTH-surf.get_width())/2,
        #(SCREEN_HEIGHT-surf.get_width())/2
   # )

    #Draw the surface to the screen
    pygame.display.flip()

