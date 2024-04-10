from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed):
        super().__init__()
        self.image= transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect =self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= self.speed
        if keys_pressed[K_s]:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]:
            self.rect.y += self.speed

class Enemy2(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if sprite.collide_rect(sprite2, sprite3):
            self.speed *= -1
        if sprite.collide_rect(sprite1, sprite3):
            self.speed *= -1
clock = time.Clock()
window = display.set_mode((700,500))
display.set_caption('Пинг понг')
background = transform.scale(image.load('Без имени3.png'), (700,500))

x2= 200
y2=100
x1= 350
y1= 250
x3=300
y3=350
sprite1 = Player('Без имени.png', 20, 200, 2)
sprite2 = Enemy('Без имени2.png', 620, 200 ,2)
sprite3 = Enemy2('gratis-png-ping-pong-thumbnail.png', 300, 200, 3)


clock = time.Clock()
FPS = 120


Game = True
while Game:
    window.blit(background,(0,0))
    sprite1.reset()
    sprite1.update()
    sprite2.reset()
    sprite2.update()
    sprite3.reset()
    sprite3.update()
    for e in event.get():
        if e.type == QUIT:
            Game = False
    display.update()
    clock.tick(FPS)

Game = True
while game:
    window.blit(background,(0,0))
    sprite1.reset()
    sprite2.reset()
    sprite1.update()
    sprite2.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
