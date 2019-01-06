import pygame,sys

import random

pygame.init()

size = (700, 933)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('下雪')
fps = 20
fclock = pygame.time.Clock()

bg = pygame.image.load('snow.jpg')
snow = []
for i in range(300):
    x = random.randrange(0, size[0])
    y = random.randrange(0, size[1])
    speedx = random.randint(-1, 2)
    speedy = random.randint(3, 5)
    snow.append([x, y, speedx, speedy])

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(bg, (0, 0))
    for i in range(len(snow)):
        pygame.draw.circle(screen, (255, 255, 255), snow[i][:2], snow[i][3])

        snow[i][0] += snow[i][2]
        snow[i][1] += snow[i][3]
        if snow[i][1] > size[1]:
            snow[i][1] = random.randrange(-10, -5)
            snow[i][0] = random.randrange(0, size[0])
    pygame.display.flip()
    #pygame.display.update()
    fclock.tick(fps)
