import math 
import random 
import pygame
swidth = 800
sheight = 500
pstartx = 370
pstarty = 380
estartymin = 50
estartymax = 150
espeedx = 4
espeedy = 25
bulletspeedy = 10
collisiond =27
pygame.init()

sccreen = pygame.display.set_mode((swidth, sheight))
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
noofenemy = 6

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
scorevlue = 0 
font = pygame.font.Font("freesansbold.ttf",32)
textx = 10
texty = 10
overfont = pygame.font.Font("freesansbold.ttf",64)
