import pygame,sys
from pygame.locals import *
import time
import random
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
clear=(0,0,0)
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
start=False
orange=(255,159,0)
down=0
up=0
left=0
right=0
x=0
y=0
x2=600
y2=600
green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)
yellow=(255,255,0)
snakex = (random.randint(0,600) // 60 ) * 60
snakey = (random.randint(0,600) // 60 ) * 60
foodx = (random.randint(0,600) // 60 ) * 60
foody = (random.randint(0,600) // 60 ) * 60
snakelist=[[snakex,snakey]]
rect_x=150
rect_x2=350
rect_y=300
rect_y2=300
def menu(start):
    while True:
        pygame.draw.rect(screen,green,(rect_x,rect_y,110,100))
        pygame.draw.rect(screen,green,(rect_x2,rect_y2,110,100))
        font = pygame.font.Font('freesansbold.ttf', 45)
        text = font.render('Play', False, orange)
        screen.blit(text,(155,320))
        text = font.render('Quit', False, orange)
        screen.blit(text,(355,320))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if 150<=event.pos[0]<=260 and 300<=event.pos[1]<=400:
                        screen.fill(clear)
                        return
                    if 350<=event.pos[0]<=450 and 300<=event.pos[1]<=400:
                        pygame.quit()
                        sys.exit()
menu(start)
score=1
game_speed=8
pygame.mixer.music.load('Low_Life_High_Life (3).mp3')
pygame.mixer.music.play(-1)
while True:
    snakelist.pop(0)
    snakelist.append([snakex,snakey])
    font = pygame.font.Font('freesansbold.ttf', 30) 
    text = font.render('Score:%d'%score, False, yellow)
    clock.tick(game_speed)
    for segment in snakelist:
        pygame.draw.rect(screen, blue, segment+[60,60])
    pygame.draw.rect(screen,red,(foodx+1,foody+1,59,59))
    y=0
    for x in range(0,600,60):
      pygame.draw.line(screen,green,(x,y),(x,y2))
    x=0
    for y in range(0,600,60):
        pygame.draw.line(screen,green,(x,y),(x2,y))
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                 if event.key == K_DOWN and not up:
                     down=1
                     up=0
                     left=0
                     right=0
                 if event.key == K_UP and not down:
                     up=1
                     down=0
                     left=0
                     right=0
                 if event.key == K_LEFT and not right:
                     left=1
                     down=0
                     up=0
                     right=0
                 if event.key == K_RIGHT and not left:
                     right=1
                     left=0
                     down=0
                     up=0
    screen.blit(text,(50,50))
    if foodx==snakex and foody==snakey:
        foodx = (random.randint(0,600) // 60 ) * 60
        foody = (random.randint(0,600) // 60 ) * 60
        snakelist.append([snakex,snakey])
        score=score+1
    if score==8:
        font = pygame.font.Font('freesansbold.ttf', 30) 
        text = font.render('Score:%d'%score, False, yellow)
        screen.blit(text,(50,50))
        pygame.display.update()
        snakelist.clear()
        snakelist=[[snakex,snakey]]
        game_speed=game_speed+2
        score=1
    if segment in snakelist[:-2]:
        screen.fill(clear)
        font = pygame.font.Font('freesansbold.ttf', 100) 
        text = font.render('Game Over', False, yellow)
        screen.blit(text,(30,300))
        font = pygame.font.Font('freesansbold.ttf', 32) 
        text = font.render('Your score is: %d'%score, False, yellow)
        screen.blit(text,(200,400))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        break
    if down==1:
        snakey=snakey+60
    if up==1:
        snakey=snakey-60
    if left==1:
        snakex=snakex-60
    if right==1:
        snakex=snakex+60
    if snakey<0:
        snakey=540
    if snakey>=600:
        snakey=0
    if snakex<0:
        snakex=540
    if snakex>=600:
        snakex=0
    pygame.display.update()
    screen.fill(clear)
