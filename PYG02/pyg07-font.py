import pygame,sys
import pygame.freetype


pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('pygame文字绘制')
GOLD = 255, 215, 0
RED = pygame.Color('red')
GREEN = pygame.Color('green')
f1 = pygame.freetype.Font('C://Windows//Fonts//msyh.ttc', 36)
f1rect = f1.render_to(screen, (200, 100), '鼻涕虫', fgcolor=GOLD, bgcolor=GREEN, rotation=330, size=50)
surf, f1rect1 = f1.render('百度算', fgcolor=RED, bgcolor=GREEN, rotation=30, size=50)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(surf, (200, 200))
    pygame.display.update()