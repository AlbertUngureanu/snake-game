import pygame
import time
import random


"""
Functii importante ale modulului pygame:

-> init() - initializare;
-> display.set_mode() - creaza un spatiu folosind TUPLE;
-> update() - actualizeaza ecranul
-> quit() - inchide ecranul
-> set_caption() - seteaza titlul jocului
-> event.get() - returneaza o lista cu evenimentele care sunt inregistrate de fereastra jocului
-> Surface.fill() - umple ecranul

-> time.Clock() - masuram timpul scurs
-> font.SysFont() - selectam fontul pe care vrem sa il folosim pentru text
"""

pygame.init()

disWidth = 600
disHeight = 400
dis = pygame.display.set_mode((disWidth, disHeight))

pygame.display.set_caption("Snake Game")

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)

# unde se afla acum sarpele
x1 = disWidth / 2
y1 = disHeight / 2

# dimensiune patrat
snakeBlock = 10

# unde vom muta sarpele
x1Change = 0
y1Change = 0

clock = pygame.time.Clock()
snakeSpeed = 30

fontStyle = pygame.font.SysFont('Arial', 25)
scoreFont = pygame.font.SysFont("Arial", 35)

#  Afisarea unui mesaj pe ecran
def message(msg, color):
    text = fontStyle.render(msg, True, color)
    dis.blit(text, [disWidth / 6, disHeight / 3])

#  Afisarea scorului
def yourScore(score):
    value = scoreFont.render("Your score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

#  Functie care deseneaza sarpele
def ourSnake(snakeBlock, snakeList):
    for x in snakeList:
        pygame.draw.rect(dis, black, [x[0], x[1], snakeBlock, snakeBlock])


def gameLoop():
    gameOver = False
    gameClose = False

    x1 = disWidth / 2
    y1 = disHeight / 2

    x1Change = 0
    y1Change = 0

    snakeList = []
    snakeLength = 1

    foodX = round(random.randrange(0, disWidth - snakeBlock) / 10.0) * 10.0
    foodY = round(random.randrange(0, disHeight - snakeBlock) / 10.0) * 10.0

    while not gameOver:
        while gameClose:
            dis.fill(blue)
            message("You lost! Press R to restart or Q to quit the game.", red)
            yourScore(snakeLength - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    gameClose = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_r:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1Change = -snakeBlock
                    y1Change = 0
                elif event.key == pygame.K_RIGHT:
                    x1Change = snakeBlock
                    y1Change = 0
                elif event.key == pygame.K_UP:
                    x1Change = 0
                    y1Change = -snakeBlock
                elif event.key == pygame.K_DOWN:
                    x1Change = 0
                    y1Change = snakeBlock

        if x1 >= disWidth or x1 < 0 or y1 >= disHeight or y1 < 0:
            gameClose = True

        x1 += x1Change
        y1 += y1Change

        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodX, foodY, snakeBlock, snakeBlock])

        snakeHead = [x1, y1]
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
        ourSnake(snakeBlock, snakeList)
        yourScore(snakeLength - 1)
        pygame.display.update()

        # Generearea mancarii
        if x1 == foodX and y1 == foodY:
            foodX = round(random.randrange(0, disWidth - snakeBlock) / 10.0) * 10.0
            foodY = round(random.randrange(0, disHeight - snakeBlock) / 10.0) * 10.0
            snakeLength += 1

        clock.tick(snakeSpeed)  # viteza jocului

    pygame.quit()
    quit()

gameLoop()