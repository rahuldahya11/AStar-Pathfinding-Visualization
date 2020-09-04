import pygame
import math 
from queue import PriorityQueue

# Set up display
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

# Color definition

RED = (225, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
YELLOW = (225, 225, 0)
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # Locating cell positions
    def get_pos(self):
        return self.row, self.col

    # Defining a cell that has already been examined
    def is_closed(self):
        return self.color == RED

    # Defining a cell that is in the open set
    def is_open(self):
        return self.color == GREEN

    # Defining a cell that is a barrier
    def is_barrier(self):
        return self.color == BLACK

    # Defining the start cell
    def is_start(self):
        return self.color == ORANGE

    # Defining the end (or goal) cell
    def is_end(self):
        return self.color == TURQUOISE

    # Resetting the cells
    def reset(self):
        return self.color == WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = WHITE

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs (x1 - x2) + abs (y1 - y1)

# Creating a grid
def make_grid(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows)
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid