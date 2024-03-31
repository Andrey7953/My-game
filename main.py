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
    direction = 'right'
    def update(self):
        if self.rect.x <= 0:
            self.direction = "right"
        if self.rect.x >= 600:
            self.direction = "left"


        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed 




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
sprite1 = Player('Без имени.png', 100, 100, 1)
sprite2 = Enemy('Без имени2.png', 300, 250 ,3)
sprite3 = GameSprite('gratis-png-ping-pong-thumbnail.png', 300, 200, 3)


clock = time.Clock()
FPS = 120


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
