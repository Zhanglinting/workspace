import  pygame
import  sys
import pygame.freetype


pygame.init()
size = width, height = 600, 400
speed = [1, 1]
speed1 = [1, 1]
GOLD = 255, 215, 0
BLACK = 0, 0, 0
pos = [230, 100]
pos1 = [50, 200]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('pygame文字绘制')
f1 = pygame.freetype.Font('C://Windows//Fonts//msyh.ttc', 36)
frect1 = f1.render_to(screen, pos, '王富霞', fgcolor=GOLD, size=50)
surf, frect2 = f1.render('我爱你', fgcolor=GOLD, size=50)
fps = 250
fclock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pos[0] < 0 or pos[0] + frect1.width > width:
        speed[0] = -speed[0]
    if pos[1] < 0 or pos[1] + frect1.height > height:
        speed[1] = -speed[1]
    pos[0] = pos[0] + speed[0]
    pos[1] = pos[1] + speed[1]

    if pos1[0] < 0 or pos1[0] + frect2.width > width:
        speed1[0] = -speed1[0]
    if pos1[1] < 0 or pos1[1] + frect2.height > height:
        speed1[1] = -speed1[1]

    pos1[0] = pos1[0] + speed1[0]
    pos1[1] = pos1[1] + speed1[1]

    screen.fill(BLACK)
    frect1 = f1.render_to(screen, pos, '王富霞', fgcolor=GOLD,size=50)
    surf, frect2 = f1.render('我爱你 ', fgcolor=GOLD, size=50)
    screen.blit(surf, pos1)
    pygame.display.update()
    fclock.tick(fps)