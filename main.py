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


class Grid:
    def __init__(self, rows, cols, width, height, screen):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.screen = screen
        self.rectangles = []

    def add_rectangle(self, row, col, rectangle):
        self.grid[row][col] = rectangle
        self.rectangles.append(rectangle)
        
    def draw_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                pygame.draw.rect(self.screen, (255, 255, 255), (j*self.width, i*self.height, self.width, self.height), 1)
                if self.grid[i][j]:
                    self.grid[i][j].draw()

    def handle_events(self, event):
        for rectangle in self.rectangles:
            if rectangle.rect.collidepoint(event.pos):
                rectangle.interact()

class Rectangle:
    def __init__(self, name, description, x, y, width, height, color, screen):
        self.name = name
        self.description = description
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.screen = screen

    def interact(self):
        #if self == playerrect:
        print(f"You interact with {self.name}. {self.description}")

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def set_rect(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def get_rect(self):
        return self.rect

    

#Create grid
g = Grid(8, 8, 800, 800, screen)

#Create rectangles
r0_0 = Rectangle("0,0", "", 0, 0, 100, 100, (122, 135, 146), screen)
g.add_rectangle(0, 0, r0_0)
r1_0 = Rectangle("1,0", "", 100, 0, 100, 100, (122, 135, 146), screen)
g.add_rectangle(1, 0, r1_0)
r2_0 = Rectangle("2,0", "", 200, 0, 100, 100, (122, 135, 146), screen)
g.add_rectangle(2, 0, r2_0)
r3_0 = Rectangle("3,0", "", 300, 0, 100, 100, (122, 135, 146), screen)
g.add_rectangle(3, 0, r3_0)
r4_0 = Rectangle("4,0", "", 400, 0, 100, 100, (122, 135, 146), screen)
g.add_rectangle(4, 0, r4_0)
r5_0 = Rectangle("5,0", "", 500, 0, 100, 100, (122, 135, 146), screen)
g.add_rectangle(5, 0, r5_0)
r6_0 = Rectangle("6,0", "", 600, 0, 100, 100, (122, 135, 146), screen)
g.add_rectangle(6, 0, r6_0)
r7_0 = Rectangle("7,0", "", 700, 0, 100, 100, (122, 135, 146), screen)
g.add_rectangle(7, 0, r7_0)
r0_1 = Rectangle("0,1", "", 0, 100, 100, 100, (122, 135, 146), screen)
g.add_rectangle(0, 1, r0_1)
r1_1 = Rectangle("1,1", "", 100, 100, 100, 100, (122, 135, 146), screen)
g.add_rectangle(1, 1, r1_1)
r2_1 = Rectangle("2,1", "", 200, 100, 100, 100, (122, 135, 146), screen)
g.add_rectangle(2, 1, r2_1)
r3_1 = Rectangle("3,1", "", 300, 100, 100, 100, (122, 135, 146), screen)
g.add_rectangle(3, 1, r3_1)
r4_1 = Rectangle("4,1", "", 400, 100, 100, 100, (122, 135, 146), screen)
g.add_rectangle(4, 1, r4_1)
r5_1 = Rectangle("5,1", "", 500, 100, 100, 100, (122, 135, 146), screen)
g.add_rectangle(5, 1, r5_1)
r6_1 = Rectangle("6,1", "", 600, 100, 100, 100, (122, 135, 146), screen)
g.add_rectangle(6, 1, r6_1)
r7_1 = Rectangle("7,1", "", 700, 100, 100, 100, (122, 135, 146), screen)
g.add_rectangle(7, 1, r7_1)
r0_2 = Rectangle("0,2", "", 0, 200, 100, 100, (122, 135, 146), screen)
g.add_rectangle(0, 2, r0_2)
r1_2 = Rectangle("1,2", "", 100, 200, 100, 100, (122, 135, 146), screen)
g.add_rectangle(1, 2, r1_2)
r2_2 = Rectangle("2,2", "", 200, 200, 100, 100, (122, 135, 146), screen)
g.add_rectangle(2, 2, r2_2)
r3_2 = Rectangle("3,2", "", 300, 200, 100, 100, (122, 135, 146), screen)
g.add_rectangle(3, 2, r3_2)
r4_2 = Rectangle("4,2", "", 400, 200, 100, 100, (122, 135, 146), screen)
g.add_rectangle(4, 2, r4_2)
r5_2 = Rectangle("5,2", "", 500, 200, 100, 100, (122, 135, 146), screen)
g.add_rectangle(5, 2, r5_2)
r6_2 = Rectangle("6,2", "", 600, 200, 100, 100, (122, 135, 146), screen)
g.add_rectangle(6, 2, r6_2)
r7_2 = Rectangle("7,2", "", 700, 200, 100, 100, (122, 135, 146), screen)
g.add_rectangle(7, 2, r7_2)
r0_3 = Rectangle("0,3", "", 0, 300, 100, 100, (122, 135, 146), screen)
g.add_rectangle(0, 3, r0_3)
r1_3 = Rectangle("1,3", "", 100, 300, 100, 100, (122, 135, 146), screen)
g.add_rectangle(1, 3, r1_3)
r2_3 = Rectangle("2,3", "", 200, 300, 100, 100, (122, 135, 146), screen)
g.add_rectangle(2, 3, r2_3)
r3_3 = Rectangle("3,3", "", 300, 300, 100, 100, (122, 135, 146), screen)
g.add_rectangle(3, 3, r3_3)
r4_3 = Rectangle("4,3", "", 400, 300, 100, 100, (122, 135, 146), screen)
g.add_rectangle(4, 3, r4_3)
r5_3 = Rectangle("5,3", "", 500, 300, 100, 100, (122, 135, 146), screen)
g.add_rectangle(5, 3, r5_3)
r6_3 = Rectangle("6,3", "", 600, 300, 100, 100, (122, 135, 146), screen)
g.add_rectangle(6, 3, r6_3)
r7_3 = Rectangle("7,3", "", 700, 300, 100, 100, (122, 135, 146), screen)
g.add_rectangle(7, 3, r7_3)
r0_4 = Rectangle("0,4", "", 0, 400, 100, 100, (122, 135, 146), screen)
g.add_rectangle(0, 4, r0_4)
r1_4 = Rectangle("1,4", "", 100, 400, 100, 100, (122, 135, 146), screen)
g.add_rectangle(1, 4, r1_4)
r2_4 = Rectangle("2,4", "", 200, 400, 100, 100, (122, 135, 146), screen)
g.add_rectangle(2, 4, r2_4)
r3_4 = Rectangle("3,4", "", 300, 400, 100, 100, (122, 135, 146), screen)
g.add_rectangle(3, 4, r3_4)
r4_4 = Rectangle("4,4", "", 400, 400, 100, 100, (122, 135, 146), screen)
g.add_rectangle(4, 4, r4_4)
r5_4 = Rectangle("5,4", "", 500, 400, 100, 100, (122, 135, 146), screen)
g.add_rectangle(5, 4, r5_4)
r6_4 = Rectangle("6,4", "", 600, 400, 100, 100, (122, 135, 146), screen)
g.add_rectangle(6, 4, r6_4)
r7_4 = Rectangle("7,4", "", 700, 400, 100, 100, (122, 135, 146), screen)
g.add_rectangle(7, 5, r7_4)
r0_5 = Rectangle("0,5", "", 0, 500, 100, 100, (122, 135, 146), screen)
g.add_rectangle(0, 5, r0_5)
r1_5 = Rectangle("1,5", "", 100, 500, 100, 100, (122, 135, 146), screen)
g.add_rectangle(1, 5, r1_5)
r2_5 = Rectangle("2,5", "", 200, 500, 100, 100, (122, 135, 146), screen)
g.add_rectangle(2, 5, r2_5)
r3_5 = Rectangle("3,5", "", 300, 500, 100, 100, (122, 135, 146), screen)
g.add_rectangle(3, 5, r3_5)
r4_5 = Rectangle("4,5", "", 400, 500, 100, 100, (122, 135, 146), screen)
g.add_rectangle(4, 5, r4_5)
r5_5 = Rectangle("5,5", "", 500, 500, 100, 100, (122, 135, 146), screen)
g.add_rectangle(5, 5, r5_5)
r6_5 = Rectangle("6,5", "", 600, 500, 100, 100, (122, 135, 146), screen)
g.add_rectangle(6, 5, r6_5)
r7_5 = Rectangle("7,5", "", 700, 500, 100, 100, (122, 135, 146), screen)
g.add_rectangle(7, 5, r7_5)
r0_6 = Rectangle("0,7", "", 0, 600, 100, 100, (122, 135, 146), screen)
g.add_rectangle(0, 6, r0_6)
r1_6 = Rectangle("1,6", "", 100, 600, 100, 100, (122, 135, 146), screen)
g.add_rectangle(1, 6, r1_6)
r2_6 = Rectangle("2,6", "", 200, 600, 100, 100, (122, 135, 146), screen)
g.add_rectangle(2, 6, r2_6)
r3_6 = Rectangle("3,6", "", 300, 600, 100, 100, (122, 135, 146), screen)
g.add_rectangle(3, 6, r3_6)
r4_6 = Rectangle("4,6", "", 400, 600, 100, 100, (122, 135, 146), screen)
g.add_rectangle(4, 6, r4_6)
r5_6 = Rectangle("5,6", "", 500, 600, 100, 100, (122, 135, 146), screen)
g.add_rectangle(5, 6, r5_6)
r6_6 = Rectangle("6,6", "", 600, 600, 100, 100, (122, 135, 146), screen)
g.add_rectangle(6, 6, r6_6)
r7_6 = Rectangle("7,6", "", 700, 600, 100, 100, (122, 135, 146), screen)
g.add_rectangle(7, 6, r7_6)
r0_7 = Rectangle("0,7", "", 0, 700, 100, 100, (122, 135, 146), screen)
g.add_rectangle(0, 7, r0_7)
r1_7 = Rectangle("1,7", "", 100, 700, 100, 100, (122, 135, 146), screen)
g.add_rectangle(1, 7, r1_7)
r2_7 = Rectangle("2,7", "", 200, 700, 100, 100, (122, 135, 146), screen)
g.add_rectangle(2, 7, r2_7)
r3_7 = Rectangle("3,7", "", 300, 700, 100, 100, (122, 135, 146), screen)
g.add_rectangle(3, 7, r3_7)
r4_7 = Rectangle("4,7", "", 400, 700, 100, 100, (122, 135, 146), screen)
g.add_rectangle(4, 7, r4_7)
r5_7 = Rectangle("5,7", "", 500, 700, 100, 100, (122, 135, 146), screen)
g.add_rectangle(5, 7, r5_7)
r6_7 = Rectangle("6,7", "", 600, 700, 100, 100, (122, 135, 146), screen)
g.add_rectangle(6, 7, r6_7)
r7_7 = Rectangle("7,7", "", 700, 700, 100, 100, (122, 135, 146), screen)
g.add_rectangle(7, 7, r7_7)

#create the player
player = pygame.image.load("omori-sprite.png")
player = pygame.transform.scale(player, (100, 100))
playerrect = Rectangle("PlayerCharacter1", "look at lil guy go", 0, 0, 100, 100, (122, 135, 146), screen)
g.add_rectangle(0, 0, playerrect)
#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            g.handle_events(event)
    # the background
    screen.fill(background)
    
    # draws the grid
    g.draw_grid()
    for y in range(height):
        for x in range(width):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(screen, (0,0,0), rect, 1)
    # draws the player
    screen.blit(player, playerrect)
    pygame.display.flip()
    clock.tick(30)