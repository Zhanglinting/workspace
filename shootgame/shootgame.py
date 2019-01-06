import pygame
import random
import time
import sys
import pygame.freetype


class SetImg(object):

        bgImage = pygame.image.load('background.png')
        WIDTH, HEIGHT = 400, 654
        start = pygame.image.load('start.png')
        pause = pygame.image.load('pause.png')
        gameover = pygame.image.load('gameover.png')
        hero0 = pygame.image.load('hero0.png')
        hero1 = pygame.image.load('hero1.png')
        bulletImg = pygame.image.load('bullet.png')
        beeImg = pygame.image.load('bee.png')
        bigplaneImg = pygame.image.load('bigplane.png')
        airplaneImg = pygame.image.load('airplane.png')
        beeEmbers = []
        airplaneEmbers = []
        bigplaneEmbers = []
        heroEmbers = []
        for i in range(4):
            beeEmbers.append(pygame.image.load('bee_ember' + str(i) + '.png'))
            airplaneEmbers.append(pygame.image.load('airplane_ember{}.png'.format(i)))
            bigplaneEmbers.append(pygame.image.load('bigplane_ember{}.png'.format(i)))
            heroEmbers.append(pygame.image.load('hero_ember{}.png'.format(i)))
        screen = pygame.display.set_mode((WIDTH, HEIGHT))


class FlyingObejct(object):

    def __init__(self, x, y, image, embers):
        self.embers = embers
        self.x = x
        self.y = y
        self.width = image.get_rect()[2]
        self.height = image.get_rect()[3]
        self.image = image

    def outOfBounds(self):
        pass

    def step(self):
        pass

    def shootBy(self, bullet):
        if bullet.isBomb():
            return False
        x1 = self.x
        x2 = self.x + self.width
        y1 = self.y
        y2 = self.y + self.height
        x = bullet.x
        y = bullet.y
        shoot = x1 < x < x2 and y1 < y < y2
        if shoot:
            bullet.setBomb(True)
        return shoot

    def blitme(self):
        SetImg.screen.blit(self.image, (self.x, self.y))


class Hero(FlyingObejct):

    def __init__(self):
        self.images = [SetImg.hero0, SetImg.hero1]
        self.image = SetImg.hero0
        self.embers = SetImg.heroEmbers
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]
        self.x = 150
        self.y = 500
        super(Hero, self).__init__(self.x, self.y, self.image, self.embers)
        self.life = 3
        self.doubleFire = 0
        self.index = 0

    def isDoubleFire(self):
        return self.doubleFire

    def addDoubleFire(self):
        self.doubleFire += 40

    def clearDoubleFire(self):
        self.doubleFire = 0

    def addLife(self):
        self.life += 1

    def subLIfe(self):
        self.life -= 1

    def getLife(self):
        return self.life

    def resetLife(self):
        self.life = 3
        self.clearDoubleFire()

    def outOfBounds(self):
        return self.x < 0 or self.x > SetImg.WIDTH - self.width or self.y < 0 or self.y > SetImg.HEIGHT - self.height

    def move(self, x, y):
        self.x = x - self.width / 2
        self.y = y - self.height / 2

    def step(self):
        #动态显示飞机
        if len(self.images) > 0:
            self.index += 1
            self.index %= len(self.images)
            self.image = self.images[self.index]

    def shoot(self):
        xStep = int(self.width /4)
        yStep = 10
        yStep1 = 5
        if self.doubleFire > 100:
            bullets = [Bullet(self.x + xStep, self.y - yStep1), Bullet(self.x + 2*xStep, self.y - yStep), Bullet(self.x + 3*xStep, self.y - yStep1)]
        elif self.doubleFire > 0:
            bullets = [Bullet(self.x + xStep, self.y - yStep1), Bullet(self.x + 3*xStep, self.y - yStep1)]
        else:
            bullets = [Bullet(self.x + 2*xStep, self.y - yStep)]
        return bullets

    def hit(self, other):
        x1 = other.x - self.width / 2
        x2 = other.x + self.width / 2 + other.width
        y1 = other.y - self.height / 2
        y2 = other.y + self.height / 2 + other.height
        x = self.x + self.width / 2
        y = self.y + self.height
        return x1 < x < x2 and y1 < y < y2


class Enemy(object):
    def getScore(self):
        pass


class Award(object):
     DOUBLE_FIRE = 0
     LIFE = 1

     def getType(self):
         pass


class Bullet(FlyingObejct):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = SetImg.bulletImg
        self.bomb = False
        #super(Bullet, self).__init__(x, y, self.image)

    def setBomb(self, bomb):
        self.bomb = bomb

    def isBomb(self):
        return self.bomb

    def step(self):
        self.y -= 2

    def outOfBounds(self):
        return self.y < 0


class Airplane(FlyingObejct, Enemy):

    def __init__(self):
        self.embers = SetImg.airplaneEmbers
        self.image = SetImg.airplaneImg
        self.width, self.height = self.image.get_rect()[2], self.image.get_rect()[3]
        self.y = - self.height
        self.x = random.randint(0, SetImg.WIDTH - self.width)
        super(Airplane, self).__init__(self.x, self.y, self.image, self.embers)

    def getScore(self):
        return 1

    def outOfBounds(self):
        return self.y > SetImg.HEIGHT

    def step(self):
        self.y += 2


class Bee(FlyingObejct, Award):

    def __init__(self):
        self.embers = SetImg.beeEmbers
        self.image = SetImg.beeImg
        self.width, self.height = self.image.get_rect()[2], self.image.get_rect()[3]
        self.x = random.randint(0, SetImg.WIDTH - self.width)
        self.y = -self.height
        self.awardType = random.randint(0, 1)
        self.speed = 1
        super(Bee, self).__init__(self.x, self.y, self.image, self.embers)

    def getType(self):
        return self.awardType

    def outOfBounds(self):
        return self.y > SetImg.HEIGHT

    def step(self):
        self.x += self.speed
        self.y += 2
        if self.x > SetImg.WIDTH - self.width:
            self.speed = -1
        if self.x < 0:
            self.speed = 1


class Bigplane(FlyingObejct, Enemy):
    def __init__(self):
        self.embers = SetImg.bigplaneEmbers
        self.life = 3
        self.image = SetImg.bigplaneImg
        self.width, self.height = self.image.get_rect()[2], self.image.get_rect()[3]
        self.y = -self.height
        self.x = random.randint(0, SetImg.WIDTH - self.width)
        super(Bigplane, self).__init__(self.x, self.y, self.image, self.embers)

    def getScore(self):
        return 3

    def outOfBounds(self):
        return self.y > SetImg.HEIGHT

    def step(self):
        self.y += 1

    def shootBy(self, bullet):
        if super(Bigplane, self).shootBy(bullet):
            self.life -= 1
        return self.life == 0


class Ember(object):
    def __init__(self, obj):
        self.embers = obj.embers
        self.image = obj.image
        self.x = obj.x
        self.y = obj.y
        self.index = 0
        self.i = 0
        self.interval = 10

    def burnDown(self):
        self.i += 1
        if self.i % self.interval == 0:
            if self.index == len(self.embers):
                return True
            self.image = self.embers[self.index]
            self.index += 1
        return False

    def blitEmber(self):
        SetImg.screen.blit(self.image, (self.x, self.y))



#游戏状态
START = 0
RUNNING = 1
PAUSE = 2
GAME_OVER = 3
state = START

hero = Hero()
flyings = []
bullets = []
embers = []
score = 0


def nextOne():
    tp = random.randint(0, 20)
    if tp < 2:
        return Bee()
    elif 1< tp < 4:
        return Bigplane()
    else:
        return Airplane()


def blit_state():
    if state == START:
        SetImg.screen.blit(SetImg.start, (0, 0))
    elif state == PAUSE:
        SetImg.screen.blit(SetImg.pause, (0, 0))
    elif state == GAME_OVER:
        SetImg.screen.blit(SetImg.gameover, (0, 0))


def blit_score():

    f1rect1 = f1.render_to(SetImg.screen, (10, 10), '生命值:{}'.format(hero.getLife()))
    f1rect2 = f1.render_to(SetImg.screen, (10, 31), '火力值:{}'.format(hero.isDoubleFire()))
    f1rect3 = f1.render_to(SetImg.screen, (330, 10), 'score:{}'.format(score))


def blit_hero():
    hero.blitme()


def blit_flyings():
    global flyings
    for fly in flyings:
        fly.blitme()


def blit_bullets():
    global bullets
    for bullet in bullets:
        bullet.blitme()

def blit_embers():
    global  embers
    for e in embers:
        e.blitEmber()

def blitme():
    blit_hero()
    blit_flyings()
    blit_bullets()
    blit_score()
    blit_state()
    blit_embers()

def emberAction():
    embersLive = []
    global  embers
    for e in embers:
        if not e.burnDown():
            embersLive.append(e)
    embers = embersLive


flyingsIndex = 0
def enterAction():
    global  flyingsIndex
    flyingsIndex += 1
    if flyingsIndex % 40 == 0:
        obj = nextOne()
        flyings.append(obj)


shootIndex = 0
def shootAction():
    global  shootIndex
    shootIndex += 1
    if shootIndex % 30 == 0:
        bs = hero.shoot()
        for b in bs:
            bullets.append(b)


def stepAction():
    hero.step()
    for f in flyings:
        f.step()
    for b in bullets:
        b.step()


def outOfBoundsAction():
    global  flyings
    flyingsLive = []
    for f in flyings:
        if not f.outOfBounds():
            flyingsLive.append(f)
    flyings = flyingsLive
    global  bullets
    bulletsLive = []
    for b in bullets:
        if not b.outOfBounds():
            bulletsLive.append(b)
    bullets = bulletsLive


def bang(b):
    for f in flyings:
        if f.shootBy(b):
            ember = Ember(f)
            embers.append(ember)
            if isinstance(f, Enemy):
                global score
                score += f.getScore()
            if isinstance(f, Award):
                if f.getType() == Award.DOUBLE_FIRE:
                    hero.addDoubleFire()
                else:
                    hero.addLife()
            flyings.remove(f)
            bullets.remove(b)


def bangAction():
    for b in bullets:
        bang(b)


def checkGameoverAction():
    if isGameover():
        global  state
        state = GAME_OVER

def isGameover():
    for f in flyings:
        if hero.hit(f):
            hero.subLIfe()
            hero.clearDoubleFire()
            e = Ember(hero)
            embers.append(e)
            flyings.remove(f)
            ember = Ember(f)
            embers.append(ember)
    return hero.getLife() <= 0


def action():
    global state
    blitme()
    x, y = pygame.mouse.get_pos()
    if state == RUNNING:
        global hero
        hero.move(x, y)
        enterAction()
        shootAction()
        stepAction()
        outOfBoundsAction()
        bangAction()
        checkGameoverAction()
        emberAction()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #鼠标点击
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag = pygame.mouse.get_pressed()[0] #左键单击事件
            rflag = pygame.mouse.get_pressed()[2] #右键单击事件
            if flag and state == START:
                state = RUNNING
            if flag and state == GAME_OVER:
                global flyings, bullets, score,embers
                flyings = []
                bullets = []
                embers = []
                hero = Hero()
                score = 0
                state = START
            if rflag:
                state = PAUSE
            if flag and state == PAUSE:
                state = RUNNING
                #鼠标移动
        '''if event.type == pygame.MOUSEMOTION:
            print(event.pos[0], event.pos[1])
            if state != GAME_OVER:
                if event.pos[0] <= 0 or event.pos[0] >= SetImg.WIDTH or event.pos[1] <= 0 or event.pos[1] >= SetImg.HEIGHT:
                    state = PAUSE
            if state == PAUSE:
                if 0 < event.pos[0] < SetImg.WIDTH and 0 < event.pos[1] < SetImg.HEIGHT:
                    state = RUNNING
        '''





if __name__ == '__main__':
        pygame.init()
        pygame.display.set_caption("飞机大战")
        f1 = pygame.freetype.Font('font//msyh.ttc', 16)
        while True:
            SetImg.screen.blit(SetImg.bgImage, (0, 0))
            action()
            pygame.display.update()







