import math 
import random 
import pygame
swidth = 800
sheight = 500
pstartx = 370
pstarty = 380
estartymin = 50
estartymax = 150
espeedx = 2
espeedy = 10
bulletspeedy = 10
collisiond =27
pygame.init()

screen = pygame.display.set_mode((swidth, sheight))
background = pygame.image.load("background (2).png")
pygame.display.set_caption("space invadors")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
playerimg = pygame.image.load("player.png")
playerX = pstartx
playery = pstarty
playerx_change = 0

enemyimg = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []
noofenemy = 7

for i in range(noofenemy):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyx.append(random.randint(0,swidth-64))
    enemyy.append(random.randint(estartymin,estartymax))
    enemyxchange.append(espeedx)
    enemyychange.append(espeedy)

bulletimg = pygame.image.load("bullet.png")
bulletx = 0
bullety = pstarty
bulletxchange = 0
bulletychange = bulletspeedy
bulletstate = "ready"
scorevalue = 0 
font = pygame.font.Font("freesansbold.ttf",32)
textx = 10
texty = 10
overfont = pygame.font.Font("freesansbold.ttf",64)
def show_score(x, y):
    # Display the current score on the screen.
    score = font.render("Score : " + str(scorevalue), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    # Display the game over text
    over_text = overfont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

def fire_bullet(x, y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < collisiond
while True:
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = +5
            if event.key == pygame.K_SPACE:
                if bulletstate == "ready":
                    bulletx = playerX
                    fire_bullet(bulletx, bullety)

        if event.type == pygame.KEYUP and event.key in[pygame.K_LEFT, pygame.K_RIGHT]:
            playerx_change = 0
    playerX += playerx_change
    playerX = max(0, min(playerX, swidth - 64))
    for i in range(noofenemy):
        if enemyy[i] > 340:
            for j in range(noofenemy):
                enemyy[j] = 2000
            game_over_text()
            break

        enemyx[i] += enemyxchange[i]
        if enemyx[i] <= 0 or enemyx[i] >= swidth - 64:
            enemyxchange[i] *= -1
            enemyy[i] += enemyychange[i]
        if isCollision(enemyx[i], enemyy[i], bulletx, bullety):
            bullety = pstarty
            bulletstate = "ready"
            scorevalue += 1
            enemyx[i] = random.randint(0, swidth - 64)
            enemyy[i] = random.randint(estartymin, estartymax)
        enemy(enemyx[i],enemyy[i],i)
    if bullety <= 0:
        bullety = pstarty
        bulletstate = "ready"
    elif bulletstate == "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bulletychange
    player(playerX, playery)
    show_score(textx, texty)
    pygame.display.update()
           

