import pygame
import random

pygame.init()

screen = pygame.display.set_mode((750, 600))
pygame.display.set_caption("Tetris")

font = pygame.font.SysFont('consolas', 30)

GRID_SIZE = 25
GRAY = (128,128,128)
BOX_COLOURS = [None,(255,0,0),(0,32,255),(0,192,0),(255,255,0)]
# RED, BLUE, GREEN, YELLOW

grid = [[0 for i in range(10)] for i in range(20)]

class player:
    def __init__(self):
        self.grid_x = 0
        self.grid_y = 0
        self.score = 0
        self.lines = 0

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
            pygame.draw.rect(screen, GRAY, (100+i*GRID_SIZE, 50+j*GRID_SIZE, GRID_SIZE, GRID_SIZE),1)
            if grid[j][i] != 0:
                colour_code = grid[j][i]
                pygame.draw.rect(screen, BOX_COLOURS[colour_code], (1+100 + i * GRID_SIZE, 1+50 + j * GRID_SIZE, GRID_SIZE-2, GRID_SIZE-2))

    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, GRAY, (490+i*GRID_SIZE, 300+j*GRID_SIZE, GRID_SIZE, GRID_SIZE),1)

    pygame.display.update()

user = player()

while True:

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
