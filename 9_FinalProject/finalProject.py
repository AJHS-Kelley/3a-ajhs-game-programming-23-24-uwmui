import pygame
from sys import exit

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('')
clock = pygame.time.Clock()
# test_font = pygame.font.Font('', 50)
game_active = True

pygame.display.update()
clock.tick(60)