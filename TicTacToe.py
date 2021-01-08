import pygame as pg, sys
import time
from pygame.locals import *


XO = 'o'
winner = None
draw = False
width = 400
height = 400
white = (255,255,255)
line_color = (10,10,10)

# Board
TTT = [[None]*3,[None]*3, [None]*3]

# Window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100))
pg.display.set_caption("Tic Tac Toe")

# Load image
openPic = pg.image.load("opening.png")
x = pg.image.load("x.png")
o = pg.image.load('o.png')

# resize
x = pg.transform.scale(x, (85, 85))
o = pg.transform.scale(o, (85, 85))
openPic = pg.transform.scale(openPic, (width, height+100))

def GameOpen():
    screen.blit(openPic, (0,0)) # vi tri anh hien thi
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

    # draw 4 lines
    pg.draw.line(screen, line_color, (width/3, 0), (width/3, height), 8)
    pg.draw.line(screen, line_color, (width/3*2, 0), (width/3*2, height), 8)
    pg.draw.line(screen, line_color, (0, height/3),(width, height/3), 8)
    pg.draw.line(screen, line_color, (0, height/3*2), (width, height/3*2), 8)
    Draw()

def Draw():
    global draw
    if winner is None:
        mess = XO.upper() + "'s Turn"
    else:
        mess = winner.upper() + " won!"
    if draw:
        mess = 'Game Draw!'

    font = pg.font.Font(None, 30)
    text = font.render(mess, 1, (255,255,255)) #render(text, antialias (khu rang cua), color, background=None)

    # render text into board
    screen.fill((0,0,0), (0,400,500,100))
    textRect = text.get_rect(center=(width/2, height+50))
    screen.blit(text, textRect)
    pg.display.update()

# Algothrims
def Check():
    global winner, TTT, draw
    # win rows
    for row in range(0,3):
        if((TTT[row][0]==TTT[row][1]==TTT[row][2]) and (TTT[row][0] is not None)):
            winner = TTT[row][0]
            pg.draw.line(screen, (255,0,0), (0, (row+1)*height/3-height/6),(width,(row+1)*height/3-height/6), 4)
            break
    # win column
    for col in range(0,3):
        if((TTT[0][col]==TTT[1][col]==TTT[2][col]) and (TTT[0][col] is not None)):
            winner = TTT[0][col]
            pg.draw.line(screen, (255,0,0), ((col +1)*width/3-width/6,0), ((col+1)*width/3-width/6, height), 4)
            break

    # Duong cheo
    if((TTT[0][0]==TTT[1][1]==TTT[2][2]) and (TTT[0][0] is not None)):
        winner = TTT[0][0]
        pg.draw.line(screen, (255,0,0), (50,50),(350,350), 4)

    if((TTT[0][2]==TTT[1][1]==TTT[2][0]) and (TTT[0][2] is not None)):
        winner = TTT[0][2]
        pg.draw.line(screen, (255,0,0), (350,350), (50,50), 4)

    if(all([all(row) for row in TTT]) and winner is None):
        draw = True
    Draw()

# Draw X,O on screen
def DrawXO(row, col):
    global TTT, XO, posX, posY

    if row==1:
        posX = 25
    if row==2:
        posX = width/3 + 25
    if row==3:
        posX = width/3*2 + 25

    if col==1:
        posY = 25
    if col==2:
        posY = height/3 + 25
    if col==3:
        posY = height/3*2 +25

    TTT[row-1][col-1] = XO
    if(XO == 'x'):
        screen.blit(x,(posY, posX))
        XO = 'o'
    else:
        screen.blit(o, (posY, posX))
        XO = 'x'
    pg.display.update()

# Mouse click
def MouseClick():
    # get pos of mouse
    x, y = pg.mouse.get_pos()

    # get column of mouse click
    if(x<width/3):
        col = 1
    elif(x<width/3*2):
        col = 2
    elif(x<width):
        col = 3
    else:
        col = None

    # get row of mouse click
    if(y<height/3):
        row = 1
    elif(y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None

    if(row and col and TTT[row-1][col-1] is None):
        global XO
        DrawXO(row,col)
        Check()

# play again
def ResetGame():
    global TTT, winner, XO, draw
    time.sleep(3)
    XO = 'o'
    draw = False
    GameOpen()
    winner=None
    TTT = [[None]*3, [None]*3, [None]*3]

# Run game
GameOpen()

while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            MouseClick()
            if(winner or draw):
                ResetGame()

    pg.display.update()
    CLOCK.tick(fps)




