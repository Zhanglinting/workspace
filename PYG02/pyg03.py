import pygame,sys

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('pygame自定义事件')
fps = 1
fclock = pygame.time.Clock()
num = 1

while True:
    #自定义事件
    userevent = pygame.event.Event(pygame.KEYDOWN, {'unicode': 123, "key": pygame.K_SPACE, 'mod': pygame.KMOD_ALT})
    #添加事件到事件队列
    pygame.event.post(userevent)
    num = num + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.unicode == 0:
                print('[KEYDOWN]:{}'.format(num), '#', event.key, event.mod)
            else:
                print('[KEYDOEN:{}]'.format(num), event.unicode, event.key, event.mod)
    pygame.display.update()
    fclock.tick(fps)