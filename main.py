import pygame
import random

pygame.init()

screen = pygame.display.set_mode((750, 600))
pygame.display.set_caption("Tetris")

GRID_SIZE = 25
GRAY = (128,128,128)
BOX_COLOURS = [None,(255,0,0),(0,32,255),(0,192,0),(255,255,0)]
# RED, BLUE, GREEN, YELLOW

grid = [[0 for i in range(10)] for i in range(20)]

def draw():

    for i in range(10):
        for j in range(20):
            pygame.draw.rect(screen, GRAY, (100+i*GRID_SIZE, 50+j*GRID_SIZE, GRID_SIZE, GRID_SIZE),1)
            if grid[j][i] != 0:
                colour_code = grid[j][i]
                pygame.draw.rect(screen, BOX_COLOURS[colour_code], (1+100 + i * GRID_SIZE, 1+50 + j * GRID_SIZE, GRID_SIZE-2, GRID_SIZE-2))

    pygame.display.update()

while True:

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
