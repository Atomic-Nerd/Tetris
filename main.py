import pygame
import random

pygame.init()

screen = pygame.display.set_mode((750, 600))
pygame.display.set_caption("Tetris")

font = pygame.font.SysFont('consolas', 30)

GRID_SIZE = 25
GRAY = (128,128,128)
RED = (255,0,0)
BLUE = (0,32,255)
GREEN = (0,192,0)
YELLOW = (255,255,0)
BOX_COLOURS = [None,RED,BLUE,GREEN,YELLOW]

grid = [[0 for i in range(10)] for i in range(20)]

SHAPES = [
    [
        [1,1,1],
        [0,1,0],
    ],
    [
        [1,1,0],
        [0,1,1],
    ],
    [
        [0,1,1],
        [1,1,0],
    ],
    [
        [0,0,1],
        [1,1,1],
    ],
    [
        [1,1,1],
        [0,0,1],
    ],
    [
        [1,1],
        [1,1]
    ],
    [
        [1,1,1,1]
    ]
]

class player:
    def __init__(self):
        self.grid_x = 0
        self.grid_y = 0

        self.shape = SHAPES[random.randint(0,6)]
        self.next_shape = SHAPES[random.randint(0,6)]
        self.shape_colour_code = random.randint(1,4)
        self.next_shape_colour_code = random.randint(1,4)

        self.score = 0
        self.lines = 0

    def newShape(self):
        self.shape = self.next_shape
        self.shape_colour_code = self.next_shape_colour_code

        self.next_shape = SHAPES[random.randint(0,6)]
        self.next_shape_colour_code = random.randint(1,4)

def draw():

    screen.fill((0,0,0))

    scoreText = font.render(f"Score: {str(user.score)}", True, (255,255,0))
    linesText = font.render(f"Lines: {str(user.lines)}", True, (255,255,0))

    screen.blit(scoreText, (500, 100))
    screen.blit(linesText, (500, 130))

    nextText = font.render("Next:", True, (255,255,0))

    screen.blit(nextText, (500, 250))

    for i in range(10):
        for j in range(20):
            colour = GRAY
            x = 100 + i * GRID_SIZE
            y = 50 + j * GRID_SIZE
            w, h = GRID_SIZE, GRID_SIZE
            pygame.draw.rect(screen, colour, (x, y, w, h),1)
            if grid[j][i] != 0:
                colour = BOX_COLOURS[grid[j][i]]
                pygame.draw.rect(screen, colour, (x+1,y+1, w-2, h-2))

    for i in range(4):
        for j in range(4):
            colour = GRAY
            x = 490+i*GRID_SIZE
            y = 300+j*GRID_SIZE
            w, h = GRID_SIZE, GRID_SIZE
            pygame.draw.rect(screen, colour, (x, y, w, h),1)

    for i in range(len(user.next_shape)):
        for j in range(len((user.next_shape)[i])):
            if user.next_shape[i][j] != 0:
                colour = BOX_COLOURS[user.next_shape_colour_code]
                x = 1+490+j*GRID_SIZE
                y = 1+325+i*GRID_SIZE
                w, h = GRID_SIZE-2, GRID_SIZE-2
                pygame.draw.rect(screen, colour,(x,y,w,h))

    pygame.display.update()

user = player()

while True:

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
