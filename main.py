import pygame
import random
from pygame import mixer
import time

pygame.mixer.pre_init(44100, 16, 2, 4096)

pygame.init()
mixer.init()

screen = pygame.display.set_mode((750, 600))
pygame.display.set_caption("Tetris")

font = pygame.font.SysFont('consolas', 30)
menu_font = pygame.font.SysFont('8bitwondernominal', 40, True)

#--------- MUSIC ----------

pygame.mixer.music.load("Sounds/background_music.wav")

# -----------------
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

SHAPES = [
    [
        [
            [0,0,0],
            [7,7,7],
            [0,7,0]
        ],
        [
            [0,7,0],
            [7,7,0],
            [0,7,0]
        ],
        [
            [0,7,0],
            [7,7,7],
            [0,0,0]
        ],
        [
            [0,7,0],
            [0,7,7],
            [0,7,0]
        ]
    ],
    [
        [
            [0,0,0],
            [1,1,0],
            [0,1,1],
        ],
        [
            [0,1,0],
            [1,1,0],
            [1,0,0],
        ],
        [
            [1,1,0],
            [0,1,1],
            [0,0,0],
        ],
        [
            [0,0,1],
            [0,1,1],
            [0,1,0],
        ]
    ],
    [
        [
            [0,0,0],
            [0,3,3],
            [3,3,0],
        ],
        [
            [3,0,0],
            [3,3,0],
            [0,3,0],
        ],
        [
            [0,3,3],
            [3,3,0],
            [0,0,0],
        ],
        [
            [0,3,0],
            [0,3,3],
            [0,0,3],
        ]
    ],
    [
        [
            [0,0,6],
            [6,6,6],
            [0,0,0],
        ],
        [
            [0,6,0],
            [0,6,0],
            [0,6,6],
        ],
        [
            [0,0,0],
            [6,6,6],
            [6,0,0],
        ],
        [
            [6,6,0],
            [0,6,0],
            [0,6,0],
        ]
    ],
    [
        [
            [2,0,0],
            [2,2,2],
            [0,0,0],
        ],
        [
            [0,2,2],
            [0,2,0],
            [0,2,0],
        ],
        [
            [0,0,0],
            [2,2,2],
            [0,0,2],
        ],
        [
            [0,2,0],
            [0,2,0],
            [2,2,0],
        ]
    ],
    [
        [
            [4,4],
            [4,4]
        ],
        [
            [4,4],
            [4,4]
        ],
        [
            [4,4],
            [4,4]
        ],
        [
            [4,4],
            [4,4]
        ]
    ],
    [
        [
            [0,0,0,0],
            [0,0,0,0],
            [5,5,5,5],
            [0,0,0,0]
        ],
        [
            [0,5,0,0],
            [0,5,0,0],
            [0,5,0,0],
            [0,5,0,0]
        ],
        [
            [0,0,0,0],
            [5,5,5,5],
            [0,0,0,0],
            [0,0,0,0]
        ],
        [
            [0,0,5,0],
            [0,0,5,0],
            [0,0,5,0],
            [0,0,5,0]
        ]
    ]
]

# ---- SOUND EDITTING ------

LINE_CLEAR_WAV = pygame.mixer.Sound("Sounds/line_clear.wav")
GAME_OVER_WAV = pygame.mixer.Sound("Sounds/game_over.wav")
PAUSE_WAV = pygame.mixer.Sound("Sounds/pause.wav")

MENU_SELECT_WAV = pygame.mixer.Sound("Sounds/menu_select.wav")
MENU_HOVER_WAV = pygame.mixer.Sound("Sounds/menu_hover.wav")

music_volume = 0.1
effect_volume = 0.4

pygame.mixer.music.set_volume(music_volume)
pygame.mixer.Sound.set_volume(LINE_CLEAR_WAV,effect_volume)
pygame.mixer.Sound.set_volume(GAME_OVER_WAV,effect_volume)
pygame.mixer.Sound.set_volume(PAUSE_WAV,0.2)

def determine_start_Y(shape):
    shape_index = SHAPES.index(shape)

    if shape_index < 3:
        return -2
    elif shape_index < 6:
        return -1
    else:
        return -2

class player:
    def __init__(self):
        self.shape_x = 3

        self.shape = SHAPES[random.randint(0,6)]
        self.next_shape = SHAPES[random.randint(0,6)]
        self.shape_orientation = 0

        self.shape_y = determine_start_Y(self.shape)

        self.score = 0
        self.rows = 0

    def newShape(self):
        self.shape = self.next_shape
        self.shape_x = 3
        self.shape_y = determine_start_Y(self.shape)
        self.shape_orientation = 0
        self.next_shape = SHAPES[random.randint(0,6)]

multiplier = 1.0
def draw():

    screen.fill((0,0,0))

    scoreText = font.render(f"Score: {str(user.score)}", True, (255,255,0))
    rowsText = font.render(f"Rows: {str(user.rows)}", True, (255,255,0))
    multiplierText = font.render(f"Speed: {round(multiplier,2)}x", True, (255, 255, 0))

    screen.blit(scoreText, (500, 100))
    screen.blit(rowsText, (500, 130))
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


    for i in range(len(user.next_shape[0])):
        for j in range(len((user.next_shape[0])[i])):
            if user.next_shape[0][i][j] != 0:
                colour = BOX_COLOURS[user.next_shape[0][i][j]]
                x = 1+490+j*GRID_SIZE
                y = 1+300+i*GRID_SIZE
                w, h = GRID_SIZE-2, GRID_SIZE-2
                pygame.draw.rect(screen, colour,(x,y,w,h))

    pygame.draw.rect(screen, RED, (125, 50, 250, 500), 3)
    pygame.display.update()

def returnPositions(shape,x,y):
    positions = []
    for tempX in range(len(shape)):
        for tempY in range(len(shape)):
            if shape[tempY][tempX] != 0:
                positions.append([y+tempY,x+tempX])

    return positions

def checkRow():
    global main_grid

    temp_grid = [row[:] for row in main_grid]
    completed_rows = 0
    y = 19
    while y!=-1:
        isCompleted = True
        if temp_grid[y] == ["X",0,0,0,0,0,0,0,0,0,0,"X"]:
            break
        for element in temp_grid[y]:
            if element == 0:
                isCompleted = False
                break
        if isCompleted:
            for i in range(0,y):
                row_index = y-i
                temp_grid[row_index] = temp_grid[row_index-1]
            temp_grid[0] = [0 for i in range(10)]
            temp_grid[0].insert(0, "X")
            temp_grid[0].append("X")
            completed_rows += 1
            LINE_CLEAR_WAV.play()
        else:
            y -= 1

    main_grid = [row[:] for row in temp_grid]

    user.rows += completed_rows

    score_add = [0,40,100,300,1200]
    user.score += score_add[completed_rows]

def checkEnd():
    coords = returnPositions(user.shape[user.shape_orientation],user.shape_x,user.shape_y)
    for coord in coords:
        if coord[0] < 1:
            return True
    return False

def canMove(shape,x,y,moveX,moveY):
    nextPositions = returnPositions(shape,x+moveX,y+moveY)
    for coord in nextPositions:
        x = coord[1]
        y = coord[0]
        if y>=0:
            if main_grid[y][x+1] != 0:
                return False
    return True

def moveRight():
    global temp_grid

    shape = user.shape[user.shape_orientation]
    if canMove(shape,user.shape_x,user.shape_y,1,0):
        temp_grid = [row[:] for row in main_grid]
        user.shape_x += 1
        for i in range(len(shape)):
            for j in range(len(shape)):
                if shape[j][i] != 0:
                    if 1+user.shape_y+j >= 0:
                        temp_grid[user.shape_y + j][user.shape_x + i + 1] = shape[j][i]


def moveLeft():
    global temp_grid

    shape = user.shape[user.shape_orientation]
    if canMove(shape,user.shape_x,user.shape_y,-1,0):
        temp_grid = [row[:] for row in main_grid]
        user.shape_x -= 1
        for i in range(len(shape)):
            for j in range(len(shape)):
                if shape[j][i] != 0:
                    if 1+user.shape_y+j >= 0:
                        temp_grid[user.shape_y+j][user.shape_x+i+1] = shape[j][i]

def nextOrientation(orientation_difference):
    if orientation_difference == -1:
        if user.shape_orientation == 0:
            return 3
        else:
            return user.shape_orientation-1
    else:
        if user.shape_orientation == 3:
            return 0
        else:
            return user.shape_orientation+1

def canRotate(shape,x,y,orientation_difference):

    nextShape = user.shape[nextOrientation(orientation_difference)]

    nextPositions = returnPositions(nextShape,x,y)

    for coord in nextPositions:
        x = coord[1]
        y = coord[0]
        if y >= 0:
            if main_grid[y][x + 1] != 0:
                return False
    return True

def rotateCounterClockwise():
    global temp_grid

    shape = user.shape[user.shape_orientation]
    if canRotate(shape,user.shape_x,user.shape_y,-1):

        temp_grid = [row[:] for row in main_grid]

        user.shape_orientation = nextOrientation(-1)
        shape = user.shape[user.shape_orientation]

        for i in range(len(shape)):
            for j in range(len(shape)):
                if shape[j][i] != 0:
                    if 1+user.shape_y+j >= 0:
                        temp_grid[user.shape_y+j][user.shape_x+i+1] = shape[j][i]

def rotateClockwise():
    global temp_grid

    shape = user.shape[user.shape_orientation]
    if canRotate(shape, user.shape_x, user.shape_y, 1):

        temp_grid = [row[:] for row in main_grid]

        user.shape_orientation = nextOrientation(1)
        shape = user.shape[user.shape_orientation]

        for i in range(len(shape)):
            for j in range(len(shape)):
                if shape[j][i] != 0:
                    if 1 + user.shape_y + j >= 0:
                        temp_grid[user.shape_y + j][user.shape_x + i + 1] = shape[j][i]

def moveUser():
    global multiplier, temp_grid, main_grid, play

    if canMove(user.shape[user.shape_orientation],user.shape_x,user.shape_y,0,1):
        temp_grid = [row[:] for row in main_grid]
        user.shape_y += 1
        for i in range(len(user.shape[user.shape_orientation])):
            for j in range(len(user.shape[user.shape_orientation])):
                if user.shape[user.shape_orientation][j][i] != 0:
                    if user.shape_y+j >= 0:
                        temp_grid[user.shape_y + j][user.shape_x + i + 1] = user.shape[user.shape_orientation][j][i]
    else:
        if not (checkEnd()):
            user.newShape()
            main_grid = [row[:] for row in temp_grid]
            checkRow()
            multiplier += 0.05
            drawFirst()
        else:
            if playsound: pygame.mixer.music.stop()
            GAME_OVER_WAV.play()
            play = False

def drawFirst():
    global temp_grid

    temp_grid = [row[:] for row in main_grid]
    for i in range(len(user.shape[user.shape_orientation])):
        for j in range(len(user.shape[user.shape_orientation])):
            if user.shape[user.shape_orientation][j][i] != 0:
                if user.shape_y + j >= 0:
                    temp_grid[user.shape_y + j][user.shape_x + i + 1] = user.shape[user.shape_orientation][j][i]

def drawPaused():
    s = pygame.Surface((750, 600))
    s.set_alpha(128)
    s.fill((255, 255, 255))
    screen.blit(s, (0, 0))
    pygame.display.update()

def drawtext(string,x,y):

    text_surface = menu_font.render(string, True, (255,255,255))
    screen.blit(text_surface, (x,y))

def highscore_menu():
    pass

def options_menu():
    pass

def credits_menu():
    pass

def  draw_main_menu(cursor_index,cursor_locations):

    screen.fill((0, 0, 0))
    drawtext("Main Menu", 100, 100)
    drawtext("Play", 150, 250)
    drawtext("Highscores", 150, 300)
    drawtext("Options", 150, 350)
    drawtext("Quit", 150, 400)
    cursor_y = cursor_locations[cursor_index]
    drawtext("*", 100, cursor_y)

    pygame.display.update()

def main_menu():
    global playsound
    
    cursor_index = 0
    cursor_locations = [250,300,350,400]
    playsound = True
    main_menu_loop = True

    while main_menu_loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and cursor_index > 0:
                    if playsound: MENU_HOVER_WAV.play()
                    cursor_index -= 1
                if event.key == pygame.K_s and cursor_index < 3:
                    if playsound: MENU_HOVER_WAV.play()
                    cursor_index += 1
                if event.key == pygame.K_RETURN:
                    if playsound: MENU_SELECT_WAV.play()
                    if cursor_index == 0:
                        main_menu_loop = False
                    elif cursor_index == 1:
                        highscore_menu()
                    elif cursor_index == 2:
                        options_menu()
                    elif cursor_index == 3:
                        pygame.time.wait(500)
                        quit()

        draw_main_menu(cursor_index,cursor_locations)

    main()

def main():
    global main_grid, temp_grid, user, current_time, next_move, next_rotate_right, next_rotate_left, play, first_run, multiplier, paused

    if playsound: pygame.mixer.music.play(-1, 0)

    main_grid = [[0 for i in range(10)] for i in range(20)]
    for i in range(20):
        main_grid[i].insert(0,"X")
        main_grid[i].append("X")

    main_grid.append(["X" for i in range(12)])
    temp_grid = [row[:] for row in main_grid]

    user = player()
    drawFirst()
    play = True
    paused = False
    draw()

    current_time = pygame.time.get_ticks()
    next_move = current_time + 1000  # 1s = 1000ms

    next_rotate_right = current_time + 150
    next_rotate_left = current_time + 150

    multiplier = 1.0

    first_run = True

    while play:

        pygame.time.wait(75)

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused = not paused
                if paused:
                    if playsound: pygame.mixer.music.pause()
                    PAUSE_WAV.play()
                    drawPaused()
                else:
                    PAUSE_WAV.play()
                    if playsound: pygame.mixer.music.unpause()

        if not(paused):

            current_time = pygame.time.get_ticks()

            if keys[pygame.K_s] and not(first_run):
                moveUser()
            else:
                first_run = False

            if keys[pygame.K_d]:
                moveRight()

            if keys[pygame.K_a]:
                moveLeft()

            if keys[pygame.K_e] and next_rotate_right <= current_time:
                rotateClockwise()
                next_rotate_right = current_time + 150 # 0.15s

            if keys[pygame.K_q] and next_rotate_left<= current_time:
                rotateCounterClockwise()
                next_rotate_left = current_time+ 150 # 0.15s

            if next_move <= current_time*multiplier:
                next_move = current_time*multiplier + 1000 # 1s
                moveUser()

            draw()
    del user

while True:
    main_menu()