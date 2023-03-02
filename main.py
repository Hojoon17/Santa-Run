#from operator import truediv
import sys
from matplotlib.pyplot import text
from matplotlib.textpath import text_to_path
from numpy import blackman
import pygame
import os
import random
from AnimatedSprite import*

white = (255, 255, 255)
red = (128, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)

pygame.init()
width_screen = 800
height_screen = 457
background1 = pygame.image.load('Santa_village.jpg')
background2 = background1.copy()

display_surface = pygame.display.set_mode((width_screen, height_screen))    
time_clok = pygame.time.Clock()                                             
pygame.display.set_caption("Santa run")  
startkey = True       
font = pygame.font.Font(None, 100)
startimage = font.render("Santa Run",True, red)
startimage_rect = startimage.get_rect()
startimage_rect.center = (400, 100)        
font1 = pygame.font.Font(None, 40)
startimage1 = font1.render("Press Space to Start", True, blue)
startimage1_rect = startimage1.get_rect()
startimage1_rect.center = (400, 200)                                      

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (0xec, 0xec, 0xec)
clock = pygame.time.Clock()
FPS = 30
BACKGROUND_COLOR = pygame.Color('white')
collide = 0

player = AnimatedSprite(position=(100, 240))

storm = pygame.image.load('ice1.png')
storm = pygame.transform.scale(storm, (80, 100))
storm_rect = storm.get_rect()
storm_rect.x = width_screen + 100
storm_rect.y = 255

storm_2 = pygame.image.load('ice2.png')
storm_2 = pygame.transform.scale(storm_2, (80, 100))
storm_2_rect = storm_2.get_rect()
storm_2_rect.x = width_screen + 1000
storm_2_rect.y = 250

storm_3 = pygame.image.load('ice3.png')
storm_3 = pygame.transform.scale(storm_3, (110, 110))
storm_3_rect = storm_2.get_rect()
storm_3_rect.x = width_screen + 2000
storm_3_rect.y = 200


all_sprites = pygame.sprite.Group(player) 
background1_x = 0
background2_x = 800

p_count = 0
points = 0

running = True
while collide == 0:
    while startkey:
        display_surface.blit(background1, (background1_x, 0))
        display_surface.blit(startimage, startimage_rect)
        display_surface.blit(startimage1, startimage1_rect)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    startkey = False
                    break
            pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.isSlide == False:
                    player.isJump = True
            if event.key == pygame.K_DOWN:
                if player.isJump == False:
                    player.isSlide = True
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    background1_x -= 8
    background2_x -= 8
    if(background1_x == -800):
        background1_x = 800
    if(background2_x == -800):
        background2_x = 800
    display_surface.fill(BACKGROUND_COLOR)
    display_surface.blit(background1, (background1_x, 0))
    display_surface.blit(background2, (background2_x, 0))
    player.jump()
    player.slide()
    all_sprites.update()   
    all_sprites.draw(display_surface)
    
    if abs(storm_rect.x - storm_2_rect.x) < 100:
        storm_2_rect.x += 100

    if storm_rect.x <= 0:
        storm_rect.x = width_screen + random.randrange(0, 500)
        storm_rect.y = 255
    storm_rect.x -= 8
    display_surface.blit(storm, storm_rect)

    if storm_2_rect.x <= 0:
        storm_2_rect.x = width_screen + random.randrange(0, 1000)
        storm_2_rect.y = 250
    storm_2_rect.x -= 8
    display_surface.blit(storm_2, storm_2_rect)

    if abs(storm_rect.x - storm_3_rect.x) < 200:
        storm_3_rect.x += 100

    if abs(storm_2_rect.x - storm_3_rect.x) < 200:
        storm_3_rect.x += 100

    if storm_3_rect.x <= 0:
        storm_3_rect.x = width_screen + random.randrange(0, 500)
        storm_3_rect.y = 200
    storm_3_rect.x -= 8
    display_surface.blit(storm_3, storm_3_rect)

    myFont = pygame.font.SysFont("arial", 18, False, True)
    text_Title = myFont.render("SCORE: ", True, BLACK)
    text_Rect = text_Title.get_rect()
    text_Rect.x = 600
    text_Rect.y = 10
    display_surface.blit(text_Title, text_Rect)

    if (p_count == 10):
        points += 1
        p_count = 0
    p_count += 1
    text_Title2 = myFont.render(str((points)), True, BLACK)
    text_Rect2 = text_Title2.get_rect()
    text_Rect2.x = 700
    text_Rect2.y = 10
    display_surface.blit(text_Title2, text_Rect2)

    if(player.rect.colliderect(storm_rect)):
        collide = 1  
    if(player.rect.colliderect(storm_2_rect)):
        collide = 1
    if(player.rect.colliderect(storm_3_rect)):
        collide = 1 

    pygame.display.update()
    clock.tick(FPS)
player.isDead = True
while(player.isDead):
    display_surface.blit(background1, (background1_x, 0))
    display_surface.blit(background2, (background2_x, 0))
    display_surface.blit(storm, storm_rect)
    display_surface.blit(storm_2, storm_2_rect)
    player.dead()
    all_sprites.update()   
    all_sprites.draw(display_surface)
    pygame.display.update()
pygame.quit()



