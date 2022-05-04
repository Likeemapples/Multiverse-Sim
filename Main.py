import pygame, sys, random, pickle

from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.set_num_channels(64)
pygame.display.set_caption("Everett")

# Pygame Variables
WINDOW_SIZE = (1280,720)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

universes = []

bgColor = (0,0,0)

playerSpeed = 1
playerSizeX = 100
playerSizeY = 100
bgColor1 = 0
bgColor2 = 0
bgColor3 = 0
percent = 0

seed1 = 0
seed2 = 0
seed3 = 0
seed4 = 0
iterationDone = False

currentUniverse = "0"

loadPlayerImg = pygame.image.load('Assets\TheBoi.png')
PlayerImg = pygame.transform.scale(loadPlayerImg,(playerSizeX,playerSizeY))
Player = [0,0]

while seed4 < 20 and not iterationDone:
    seed3 = 0
    while seed3 < 40:
        seed2 = 0
        while seed2 < 80:
            seed1 = 0
            while seed1 < 160:
                universes.append([seed1,seed2,seed3,seed4])
                seed1 += 1
            seed2 += 1
        seed3 += 1
    seed4 += 1
    print(str(seed4*5) + "%")
print("done")


while True:
    iterationDone = True
    screen.fill(bgColor)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_r:
                Player = [0,0]

            if event.key == K_BACKSPACE:
                currentUniverse = currentUniverse[:-1]
            elif event.key == K_0 or event.key == K_1 or event.key == K_2 or event.key == K_3 or event.key == K_4 or event.key == K_5 or event.key == K_6 or event.key == K_7 or event.key == K_8 or event.key == K_9:
                currentUniverse += event.unicode

            if event.key == K_RETURN:
                if not int(currentUniverse) >= len(universes):
                    s1 = universes[int(currentUniverse)][0]
                    s2 = universes[int(currentUniverse)][1]
                    s3 = universes[int(currentUniverse)][2]
                    s4 = universes[int(currentUniverse)][3]
                    bgColor1 = s1*1.59375
                    bgColor2 = s2*3.1875
                    bgColor3 = s3*6.375
                    bgColor = (bgColor1,bgColor2,bgColor3)
                    playerSizeX = s1*0.625 + 10
                    playerSizeY = s2*1.25 + 10
                    PlayerImg = pygame.transform.scale(loadPlayerImg,(playerSizeX,playerSizeY))
                    playerSpeed = s1/10
                else: 
                    print("no")


    currentUniverse = int(currentUniverse) + 1
    s1 = universes[int(currentUniverse)][0]
    s2 = universes[int(currentUniverse)][1]
    s3 = universes[int(currentUniverse)][2]
    s4 = universes[int(currentUniverse)][3]
    bgColor1 = s1*1.59375
    bgColor2 = s2*3.1875
    bgColor3 = s3*6.375
    bgColor = (bgColor1,bgColor2,bgColor3)
    playerSizeX = s1*0.625 + 10
    playerSizeY = s2*1.25 + 10
    PlayerImg = pygame.transform.scale(loadPlayerImg,(playerSizeX,playerSizeY))
    playerSpeed = s1/10

    keys = pygame.key.get_pressed()
    if keys[K_d] or keys[K_RIGHT]: 
        Player[0] += playerSpeed
    if keys[K_a] or keys[K_LEFT]:
        Player[0] -= playerSpeed
    if keys[K_w] or keys[K_UP]:
        Player[1] -= playerSpeed
    if keys[K_s] or keys[K_DOWN]:
        Player[1] += playerSpeed

    screen.blit(PlayerImg,Player)
    print(currentUniverse, len(universes), bgColor)
    pygame.display.flip()