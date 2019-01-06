import pygame,sys

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('pygame')
GOLD = 255, 215, 0
RED = pygame.Color('red')
GREEN = pygame.Color('green')
rect1 = pygame.draw.rect(screen, GOLD, (100, 100, 100, 100), 5)
rect2 = pygame.draw.rect(screen, RED, (200, 200, 100, 100), 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()