import pygame, sys
pygame.init()
import random
from enum import Enum

'''
-> Make a grid system
    -> Scalable to sreen
    -> Set grid size
    -> Add black bars depending on screen size

-> Make a User Interface
    -> Buttons of specific action type
        -> Buttons change UI to display all possible actions of that action type
        -> When hovered display a description of what hat ction will do
    -> Display hero icons on the side
        -> Health Points and Actions
    -> Turn order is displayed below hero icons
        -> current turn and who's next
        
-> logs
    -> logs of what has happend during combat
'''

# screen size
DISPLAY = pygame.display.Info()
# width and height of the screen
SIZE = (DISPLAY.current_w, DISPLAY.current_h)
# width and height for tiles
TILES = (8,8)
tile_size = (SIZE[1] - 200) / TILES[1]
# background colour
background = 122, 135, 146
player_x, player_y = 0,0
x_offset = (SIZE[0] - (tile_size * TILES[0])) / 2
# y_offset = (SIZE[1] - (tile_size * TILES[1])) / 2

#set the screen
screen = pygame.display.set_mode(SIZE)
#DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# name the game window and give it an icon
pygame.display.set_caption('Rat Catchers')
icon = pygame.image.load("simple_ratcatchers_icon.png")
pygame.display.set_icon(icon)
# clock for setting frames
clock = pygame.time.Clock()

#class Entitity():

# a class for creating the grid of the map
class Grid:
    # initilize function
    def __init__(self, rows, cols, width, height, screen):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.screen = screen
        self.rectangles = []
    # function for adding a rectangle into the grid matrix
    def add_rectangle(self, row, col, rectangle):
        self.grid[row][col] = rectangle
        self.rectangles.append(rectangle)
    # function for draws the grid
    def draw_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                pygame.draw.rect(self.screen, (255, 255, 255), (j*self.width, i*self.height, self.width, self.height), 1)
                if self.grid[i][j]:
                    self.grid[i][j].draw()
    # function for handling events (i.e. clicking)
    def handle_events(self, event):
        # finds which tile the click was in and calls on rectangle.interact()
        for rectangle in self.rectangles:
            if rectangle.rect.collidepoint(event.pos):
                rectangle.interact()
# a class mainly for creating tiles on the grid
class Rectangle:
    # initilize function
    def __init__(self, name : str, description, x, y, width, height, color, screen) -> None:
        self.name = name
        self.description = description
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.screen = screen
    # function for when a tile is clicked
    def interact(self) -> None:
        print(f"You interact with {self.name}. {self.description}")
    # function for drawing the rectangle
    def draw(self) -> None:
        pygame.draw.rect(self.screen, self.color, self.rect)

# initialize grid
g = Grid(12, 8, SIZE[0], SIZE[1], screen)

# create and add rectangles to grid
for i in range(TILES[0]):
    for j in range(TILES[1]):
        rect = Rectangle(f"{i},{j}", "", j*tile_size + x_offset, i*tile_size, tile_size, tile_size, (122, 135, 146), screen)
        g.add_rectangle(i, j, rect)

#images fpr each tile
grass_tile = pygame.image.load("grass_tile.jpg")
grass_tile = pygame.transform.scale(grass_tile, (tile_size, tile_size))
water_tile = pygame.image.load("water_tile.jpg")
water_tile = pygame.transform.scale(water_tile, (tile_size, tile_size))
wood_tile = pygame.image.load("wood_tile.jpg")
wood_tile = pygame.transform.scale(wood_tile, (tile_size, tile_size))

#create the player
player = pygame.image.load("Primalist_Sprite.png")
player = pygame.transform.scale(player, (tile_size, tile_size))
playerrect = Rectangle("PlayerCharacter1", "look at lil guy go", (player_x * tile_size) + x_offset, 
            (player_y * tile_size), tile_size, tile_size, (122, 135, 146), screen)
g.add_rectangle(0, 0, playerrect)



#main loop
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT: sys.exit()
        # detects if the user has clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            g.handle_events(event)
        elif event.type == pygame.KEYDOWN and event.key == 27:
            sys.exit()

    # the background
    screen.fill(background)
    
    # creates the grid
    g.draw_grid()

    # draws the tiles
    for row in range(TILES[0]):
        for col in range(TILES[1]):
            # draws the water tiles
            if (col >= 8 - row and col <= 10 - row):
                screen.blit(water_tile, (col*tile_size + x_offset, row*tile_size))
            # draws the grass tiles
            else:
                screen.blit(grass_tile, (col*tile_size + x_offset, row*tile_size))
            # draws the wood tiles
            if ((row == 4 and (col >= 3 and col <= 5)) or (row == 5 and (col >= 4 and col <= 6))):
                screen.blit(wood_tile, (col*tile_size + x_offset, row*tile_size))
            rect = pygame.Rect(col*tile_size + x_offset, row*tile_size, tile_size, tile_size)
            pygame.draw.rect(screen, (0,0,0), rect, 1)
            
    # draws the playerA
    screen.blit(player, playerrect)

    # updates the parts of the screen that need to be
    pygame.display.flip()
    # caps the fps at 60
    clock.tick(60)