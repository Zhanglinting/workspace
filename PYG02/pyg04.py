#色彩机制
import pygame, sys


pygame.init()
#获得屏幕相关信息
info = pygame.display.Info()
size = width, height = 600, 400
speed = [1, 1]
BLACK = 0, 0, 0
#设置游戏图标
icon = pygame.image.load('ball.gif')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
#screen = pygame.display.set_mode(size, pygame.NOFRAME)
#screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption('壁球运动')
surface = pygame.display.get_caption()
print(surface)
ball = pygame.image.load('ball.gif')
ballrect = ball.get_rect()
#控制小球刷新频率
fps = 400
fclock = pygame.time.Clock()
still = True
#获得颜色类
bgcolor = pygame.Color('black')

def RGBChanel(a):
    return 0 if a < 0 else (255 if a > 255 else int(a))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0])-1)*(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0]-1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1])-1)*(speed[1]/abs(speed[1]))
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
                #游戏窗口大小可调
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            #鼠标控制运动
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                still = True
                #ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
    #游戏感知，最小化时游戏暂停，最大化游戏继续
    if pygame.display.get_active() and still:
        ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
        if ballrect.right > width and ballrect.right + speed[0] > ballrect.right:
            speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]
        if ballrect.bottom > height and ballrect.bottom + speed[1] > ballrect.bottom:
            speed[1] = - speed[1]
    bgcolor.r = RGBChanel(ballrect.left*255/width)
    bgcolor.g = RGBChanel(ballrect.bottom*255/height)
    bgcolor.b = RGBChanel(min(speed[0], speed[1])*255/max(speed[0], speed[1]))
    #screen.fill(BLACK)
    screen.fill(bgcolor)
    screen.blit(ball, ballrect)
    pygame.display.update()
    #控制小球刷新频率
    fclock.tick(fps)
