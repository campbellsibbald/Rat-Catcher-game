import pygame, sys
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

class TileType(Enum):
    '''
    enumerator class for tile types, just makes the tile types more readable
    e.g. TileType.GRASS for grass instead of the integer 0
    '''
    GRASS = 0
    WATER = 1
    WOOD = 2

class GameObject:
    '''
    base class for anything on the grid system
    everything has an x, y, width and height
    '''
    def __init__(self, x : float, y : float, w : float, h : float):
        self.x, self.y, self.w, self.h = x, y, w, h
    def handle_event(self, event : pygame.event.Event) -> None:
        '''
        handle event function of base class, will be implemented when inherited
        '''
        pass

class Entity():
    def __init__(self) -> None:
        pass

class Player():
    '''
    class for the player (contains multiple "players" eventually)
    '''
    def __init__(self, tile_size : float):
        self.surface = pygame.transform.scale(pygame.image.load('Primalist_Sprite.png').convert_alpha(), (tile_size, tile_size))

class Tile(GameObject):
    '''
    class for a tile in the game
    '''
    def __init__(self, x: float, y: float, tile_size : float, type : TileType):
        super().__init__(x, y, tile_size, tile_size)
        # storing the tile type (TileType.GRASS, TileType.WATER, etc.)
        self.type = type
        # the object in the tile, will be of Entity type
        self.entity = None
    def render(self, surface : pygame.Surface):
        if self.entity:
            surface.blit(self.entity.surface, (self.x * self.w, self.y * self.h))
    def set_object(self, obj : Entity):
        '''
        sets the contained object to the passed Entity-type object
        '''
        self.entity = obj
    def handle_event(self, event: pygame.event.Event, grid_position : tuple) -> None:
        '''
        the implemented method for handling events (look at GameObject class)
        '''
        # similar to switch case, I heard it was faster than if statements
        match event.type:
            case pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(self.x * self.w + grid_position[0], self.y * self.h + grid_position[1], self.w, self.h).collidepoint(event.pos):
                    print('CLICKED TILE @ {} {}, TYPE {}, WITH : {}'.format(self.x, self.y, self.type, self.entity))

class Grid:
    '''
    grid class for storing all the tiles and drawing them
    '''
    def __init__(self, rows : int, cols : int, tile_size : float, tile_sprites : dict[TileType, pygame.Surface]) -> None:
        self.rows, self.cols, self.SIZE = rows, cols, tile_size
        self.tile_sprites = tile_sprites # a dictionary of surfaces to draw the tiles with, ties TileType with a Surface object
        self.tile_size = tile_size # size of a tile
        # filling a grid with random stuff using list comprehension
        self.grid = [[Tile(x, y, self.tile_size, TileType.GRASS) for x in range(cols)] for y in range(rows)]
        self.x, self.y = 0, 0
        self.surface = pygame.Surface((self.cols * self.tile_size, self.rows * self.tile_size))
    def handle_event(self, event : pygame.event.Event) -> None:
        for row in self.grid:
            for tile in row:
                tile.handle_event(event, (self.x, self.y))
    def set_tile(self, x : int, y : float, type : TileType) -> None:
        self.grid[y][x].type = type
    def render(self, surface : pygame.Surface) -> None:
        for row in self.grid:
            for tile in row:
                # will draw the tile sprite based on what type it is (using the tile_sprites dictionary)
                self.surface.blit(self.tile_sprites[tile.type], (tile.x*self.tile_size, tile.y*self.tile_size))
                # draws the black rectangle around it
                pygame.draw.rect(self.surface, (0, 0, 0), (tile.x*self.tile_size, tile.y*self.tile_size, self.tile_size, self.tile_size), 2)
                tile.render(self.surface)
        surface.blit(self.surface, (self.x, self.y))

class RatCatchers:
    def __init__(self) -> None:
        # the display info
        self.display_info = pygame.display.Info()
        # the screen size constant
        self.SIZE = (self.display_info.current_w, self.display_info.current_h)
        # the main surface to draw onto
        self.screen = pygame.display.set_mode(self.SIZE)
        # adds an icon and title to the game
        self.decorate_window()
        # constants with grid size
        ROWS, COLS = 8, 8
        self.tile_size = self.SIZE[1] / ROWS # determining the size of 1 tile based on screen height
        self.tile_dict = {}
        self.load_tile_sprites()
        self.clock = pygame.time.Clock() # clock for controlling time
        self.BG_COLOR = pygame.Color(122, 135, 146) # the base background color
        self.grid = Grid(ROWS, COLS, self.tile_size, self.tile_dict) # instantiating the new grid object
        self.grid.x = (self.SIZE[0] - (COLS * self.tile_size))/2
        self.player = Player(self.tile_size)
        self.grid.grid[3][3].set_object(self.player)
        self.done = False # to run the game later
    def load_tile_sprites(self) -> None:
        # creating the tile dictionary to tie a tile type to an image
        self.tile_dict[TileType.GRASS] = pygame.transform.scale(pygame.image.load("grass_tile.jpg").convert(), (self.tile_size, self.tile_size))
        self.tile_dict[TileType.WATER] = pygame.transform.scale(pygame.image.load("water_tile.jpg").convert(), (self.tile_size, self.tile_size))
        self.tile_dict[TileType.WOOD] = pygame.transform.scale(pygame.image.load("wood_tile.jpg").convert(), (self.tile_size, self.tile_size))
    def decorate_window(self) -> None:
        pygame.display.set_caption('Rat Catchers')
        self.icon = pygame.image.load("simple_ratcatchers_icon.png").convert()
        pygame.display.set_icon(self.icon)
    def run(self) -> None:
        '''
        the main loop of the game
        '''
        while not self.done:
            self.handle_events() # handle events
            self.tick() # update any logic
            self.render() # draw the game

    def handle_events(self) -> None:
        for event in pygame.event.get():
            print(event)
            match event.type:
                case pygame.QUIT:
                    self.done = True
            self.grid.handle_event(event) # tells the grid to handle the event
    def tick(self) -> None:
        # GAME LOGIC, NOTHING REALLY HERE
        pass
    def render(self) -> None:
        self.screen.fill(self.BG_COLOR) # fill the background with a color first
        self.grid.render(self.screen) # tells the grid to render to screen
        # eventually, add more objects that also have some sort of render function to them
        # and then add them here to render
        self.clock.tick()
        pygame.display.update() # updates the screen

if __name__ == '__main__':
    pygame.init() # initialize pygame
    game = RatCatchers() # create an instance of the game
    game.run() # call the run method (contains the main loop)
    pygame.quit() # quit pygame