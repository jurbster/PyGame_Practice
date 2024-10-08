#Game to practice and learn PyGame

import pygame
import random

from pygame.locals import(
    RLEACCEL,
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
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
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

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

#Define enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH +100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill

#Define the cloud object
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        #The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
#Create a custom event for adding a new cloud
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

#Instantiate player
player = Player()

#Create groups to hold enemy sprites, cloud sprites, and all sprites
#enemies is used for collision detection and position updates
#clouds is used for position updates
#all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#Variable that keeps the main loop running
running = True

#Setup clock for decent framerate (managable game play)
clock = pygame.time.Clock()

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

        #Add a new enemy
        elif event.type == ADDENEMY:
            #Create a new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        #Add a new cloud
        elif event.type == ADDCLOUD:
            #Create a new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    #Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    #Update the player sprite based on user keypresses
    player.update(pressed_keys)

    #Update enemy position and cloud position
    enemies.update()
    clouds.update()

    #Give the surface a color
    screen.fill((161, 208, 237))

    #Draw all the sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    #Check if any enemies collide with the player
    if pygame.sprite.spritecollideany(player, enemies):
        #If collide, then remove the player and stop loop
        player.kill
        running = False

    #Draw the surface to the screen
    pygame.display.flip()

    #Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

