import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1100,1000))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()
game_active = True
startTime = 0

title_surf = pygame.image.load('9_FinalProject\graphics/titlescreenbeta.png').convert()
title_rect = title_surf.get_rect()

start_surf = pygame.image.load('9_FinalProject\graphics/startButton.png').convert()
start_rect = start_surf.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if game_active: # What happens each 'turn' or frame of the game. 
        screen.blit(title_surf, (0,0))
        screen.blit(start_surf, (400,750))


        # transition from title screen to level 1. 
        # Display Level 1. 
        # Display Player Sprite. 
        # Display HUD 
        # Display Enemies 
        # Display Items 




    pygame.display.update()
    clock.tick(60)