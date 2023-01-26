import pygame, sys
pygame.init()

size = width, height = 800, 800
speed = [2, 2]
background = 122, 135, 146
block_size = 100
player_selected = False

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Rat Catchers')
# pygame.display.set_icon(Icon_name)
clock = pygame.time.Clock()

player = pygame.image.load("omori-sprite.png")
player = pygame.transform.scale(player, (100, 100))
playerrect = player.get_rect()

class Grid():
    def __init__(self, name, description):
        self.name = name
        self.description = description
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    # the background
    screen.fill(background)
    # draws the grid
    for y in range(height):
        for x in range(width):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(screen, (0,0,0), rect, 1)
    # draws the player
    screen.blit(player, playerrect)
    # get all events
    ev = pygame.event.get()

    # proceed events
    for event in ev:

        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if playerrect.collidepoint(pos):
                player = pygame.image.load("omori-cat.png")
                player = pygame.transform.scale(player, (100, 100))
                player_selected = True

    pygame.display.flip()
    clock.tick(30)