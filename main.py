from pygame import *
right = 0
left = 0
font.init()
font2 = font.Font(None,36)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed, player_hight, player_width):
        super().__init__()
        self.image= transform.scale(image.load(player_image), (player_hight, player_width))
        self.speed = player_speed
        self.speedX = player_speed
        self.speedY = player_speed
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
        global left
        global right
        self.rect.x += self.speedX
        self.rect.y += self.speedY
    
        if self.rect.y >= 450:
            self.speedY *= -1
        if self.rect.y <= 0:
            self.speedY *= -1


        if sprite.collide_rect(sprite2, sprite3):
            self.speedX *= -1
            

        if sprite.collide_rect(sprite1, sprite3):
            self.speedX *= -1
        
        if self.rect.x >= 650:
            self.rect.x = 350
            left += 1

        if self.rect.x <= 0:
            self.rect.x = 350
            right +=1
clock = time.Clock()
window = display.set_mode((700,500))
display.set_caption('Пинг понг')
background = transform.scale(image.load('Без имени3.png'), (1000,500))

x2= 200
y2=100
x1= 350
y1= 250
x3=300
y3=350
sprite1 = Player('Без имени.png', 20, 200, 3, 65,150)
sprite2 = Enemy('Без имени2.png', 620, 200 ,3,65,150)
sprite3 = Enemy2('gratis-png-ping-pong-thumbnail.png', 300, 200, 3,65,65)

font.init()
font3 = font.Font(None, 80)
clock = time.Clock()
FPS = 120

mixer.init()
mixer.music.load('004.mp3')
mixer.music.play()



Game = True
finish = False

while Game:
    if finish == False:
        window.blit(background,(0,0))
        sprite1.reset()
        sprite1.update()
        sprite2.reset()
        sprite2.update()
        sprite3.reset()
        sprite3.update()
    else:
        text3 = font3.render('Проиграл',1,(255,77,255))
        window.blit(text3,(250,250))

    text1 = font2.render(str(left) + ':' + str(right),1,(255,60, 255))

    window.blit(text1,(340,20))
    for e in event.get():
        if e.type == QUIT:
            Game = False
    display.update()
    clock.tick(FPS)

