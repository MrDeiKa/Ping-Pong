from pygame import *
import sys

font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, spr_image, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(spr_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Wall(GameSprite):
    def __init__(self, spr_image, x, y, size_x, size_y, speed, key1, key2):
        super().__init__(spr_image, x, y, size_x, size_y, speed)
        self.key1 = key1
        self.key2 = key2
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[self.key1] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[self.key2] and self.rect.y < 650:
            self.rect.y += self.speed
class Ball(GameSprite):
    def __init__(self, spr_image, x, y, size_x, size_y, speed, speed_y):
        super().__init__(spr_image, x, y, size_x, size_y, speed)
        self.speed_y = speed_y
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > 725:
            self.speed_y *= -1
        if sprite.collide_rect(wall1, self) or sprite.collide_rect(wall2, self):
            self.speed *= -1

window = display.set_mode((1000, 800))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("background.png"), (1000, 800))

wall1 = Wall("wall.png", 20, 325, 30, 150, 10, K_w, K_s)
wall2 = Wall("wall.png", 950, 325, 30, 150, 10, K_UP, K_DOWN)
ball = Ball("ball.png", 50, 350, 75, 75, 4, 4)

font1 = font.SysFont("Calibri", 60)
font2 = font.SysFont("Arial", 100)

clock = time.Clock()
FPS = 60
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            sys.exit()

        if e.type == KEYDOWN:
            if e.key == K_r:
                wall1 = Wall("wall.png", 20, 325, 30, 150, 10, K_w, K_s)
                wall2 = Wall("wall.png", 950, 325, 30, 150, 10, K_UP, K_DOWN)
                ball = Ball("ball.png", 50, 350, 75, 75, 4, 4)
                finish = False
            if e.key == K_q:
                    game = False

    if finish != True:    
        window.blit(background, (0, 0))
        wall1.reset()
        wall1.update()
        wall2.reset()
        wall2.update()
        ball.reset()
        ball.update()

        if ball.rect.x <= 0:
            finish = True
            lose_font = font2.render("2-Й ИГРОК ПОБЕДИЛ!", True, (255, 255, 255))
            window.blit(lose_font, (80, 240))
            more_font = font1.render("Хотите сыграть снова? (R/Q)", True, (255, 255, 255))
            window.blit(more_font, (150, 370))

        if ball.rect.x >= 980:
            finish = True
            lose_font = font2.render("1-Й ИГРОК ПОБЕДИЛ!", True, (255, 255, 255))
            window.blit(lose_font, (80, 240))
            more_font = font1.render("Хотите сыграть снова? (R/Q)", True, (255, 255, 255))
            window.blit(more_font, (150, 370))
    
    clock.tick(FPS)
    display.update()