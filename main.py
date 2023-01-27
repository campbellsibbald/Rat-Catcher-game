import pygame, sys
pygame.init()

# screen size
size = swidth, sheight = 1500, 800
# width and height for tiles
width, height = 80,80
speed = [2, 2]
# background colour
background = 122, 135, 146

#set the screen
screen = pygame.display.set_mode(size)
#DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# name the game window and give it an icon
pygame.display.set_caption('Rat Catchers')
icon = pygame.image.load("simple_ratcatchers_icon.png")
pygame.display.set_icon(icon)
# clock for setting frames
clock = pygame.time.Clock()


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
    def __init__(self, name, description, x, y, width, height, color, screen):
        self.name = name
        self.description = description
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.screen = screen
    # function for when a tile is clicked
    def interact(self):
        print(f"You interact with {self.name}. {self.description}")
    # function for drawing the rectangle
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    # function for setting new parameters for the rectangle
    def set_rect(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    # function for retreiving the rectangles parameters
    def get_rect(self):
        return self.rect

# initialize grid
g = Grid(12, 8, swidth, sheight, screen)

# create and add rectangles to grid
for i in range(4,12):
    for j in range(8):
        rect = Rectangle(f"{i},{j}", "", j*width, i*height, width, height, (122, 135, 146), screen)
        g.add_rectangle(i, j, rect)

#images fpr each tile
grass_tile = pygame.image.load("grass_tile.jpg")
grass_tile = pygame.transform.scale(grass_tile, (width, height))
water_tile = pygame.image.load("water_tile.jpg")
water_tile = pygame.transform.scale(water_tile, (width, height))
wood_tile = pygame.image.load("wood_tile.jpg")
wood_tile = pygame.transform.scale(wood_tile, (width, height))

#create the player
player = pygame.image.load("Primalist_Sprite.png")
player = pygame.transform.scale(player, (width, height))
playerrect = Rectangle("PlayerCharacter1", "look at lil guy go", 320, 0, width, height, (122, 135, 146), screen)
g.add_rectangle(0, 0, playerrect)

#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        # detects if the user has clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            g.handle_events(event)

    # the background
    screen.fill(background)
    
    # creates the grid
    g.draw_grid()

    # draws the tiles
    for row in range(8):
        for col in range(4,12):
            # draws the water tiles
            if (col >= 12 - row and col <= 14 - row):
                screen.blit(water_tile, (col*width, row*height))
            # draws the grass tiles
            else:
                screen.blit(grass_tile, (col*width, row*height))
            # draws the wood tiles
            if ((row == 4 and (col >= 7 and col <= 9)) or (row == 5 and (col >= 8 and col <= 10))):
                screen.blit(wood_tile, (col*width, row*height))
            
    # draws the grid
    for y in range(height):
        for x in range(width):
            rect = pygame.Rect(x*width, y*height, width, height)
            pygame.draw.rect(screen, (0,0,0), rect, 1)

    # draws the playerA
    screen.blit(player, playerrect)

    # updates the parts of the screen that need to be
    pygame.display.flip()
    # caps the fps at 60
    clock.tick(60)