import pygame
import random
import time

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
AQUA = (0,255,255)
ORANGE = (249,146,69)
PURPLE = (230,230,250)
BOX_COLOURS = [None,RED,BLUE,GREEN,YELLOW,AQUA,ORANGE,PURPLE]

#Creating outer bounds
main_grid = [[0 for i in range(10)] for i in range(20)]
for i in range(20):
    main_grid[i].insert(0,"X")
    main_grid[i].append("X")

main_grid.append(["X" for i in range(12)])
temp_grid = main_grid.copy()

SHAPES = [
    [
        [7,7,7],
        [0,7,0],
    ],
    [
        [1,1,0],
        [0,1,1],
    ],
    [
        [0,3,3],
        [3,3,0],
    ],
    [
        [0,0,6],
        [6,6,6],
    ],
    [
        [2,0,0],
        [2,2,2],
    ],
    [
        [4,4],
        [4,4]
    ],
    [
        [5,5,5,5]
    ]
]

class player:
    def __init__(self):
        self.main_grid_x = 0
        self.main_grid_y = 0

        self.shape = SHAPES[random.randint(0,6)]
        self.next_shape = SHAPES[random.randint(0,6)]

        self.score = 0
        self.lines = 0

    def newShape(self):
        self.shape = self.next_shape

        self.next_shape = SHAPES[random.randint(0,6)]

def draw():

    screen.fill((0,0,0))

    scoreText = font.render(f"Score: {str(user.score)}", True, (255,255,0))
    linesText = font.render(f"Lines: {str(user.lines)}", True, (255,255,0))
    multiplierText = font.render(f"Speed: {round(multiplier,2)}x", True, (255, 255, 0))

    screen.blit(scoreText, (500, 100))
    screen.blit(linesText, (500, 130))
    screen.blit(multiplierText, (500,160))

    nextText = font.render("Next:", True, (255,255,0))

    screen.blit(nextText, (500, 250))

    for i in range(1,11):
        for j in range(0,20):
            colour = GRAY
            x = 100 + i * GRID_SIZE
            y = 50 + j * GRID_SIZE
            w, h = GRID_SIZE, GRID_SIZE
            pygame.draw.rect(screen, colour, (x, y, w, h),1)
            if temp_grid[j][i] != 0:
                x += 1
                y += 1
                w -= 2
                h -= 2
                colour = BOX_COLOURS[temp_grid[j][i]]
                pygame.draw.rect(screen, colour, (x,y, w, h))

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
                colour = BOX_COLOURS[user.next_shape[i][j]]
                x = 1+490+j*GRID_SIZE
                y = 1+325+i*GRID_SIZE
                w, h = GRID_SIZE-2, GRID_SIZE-2
                pygame.draw.rect(screen, colour,(x,y,w,h))

    pygame.display.update()

user = player()

def updateGrid():
    temp
def drawPaused():
    s = pygame.Surface((750, 600))
    s.set_alpha(128)
    s.fill((255, 255, 255))
    screen.blit(s, (0, 0))
    pygame.display.update()

paused = False

current_time = pygame.time.get_ticks()

next_move = current_time + 1000 # 1s = 1000ms
multiplier = 1.0

while True:

    pygame.time.wait(10)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            paused = not paused
            if paused:
                drawPaused()

    if not(paused):

        current_time = pygame.time.get_ticks()

        if next_move <= current_time*multiplier:
            next_move = current_time*multiplier + 1000
            multiplier += 0.01


        draw()
