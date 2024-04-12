import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200,1000))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Kenney Pixel Square.ttf', 50)
game_active = True
startTime = 0

sky_surf = pygame.image.load()

score_surf = test_font.render('My game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)