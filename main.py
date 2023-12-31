from typing import Any
import pygame

width = 1300
height = 700

FPS = 60

window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.display.set_caption("Гра Пінг Понг. Автор: Аліна Білоган")

# background = pygame.transform.scale(
#                     pygame.image.load("..."), 
#                     (width, height)
#             )

background_color = (189, 0, 255)



class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x,y, speed, size):
        super().__init__()
        self.image = pygame.transform.scale(
                            pygame.image.load(image),
                            size
        )
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:    
            self.rect.y += self.speed

    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:    
            self.rect.y += self.speed



ball = GameSprite("ball.png", width/2, height/2, 0, (50,50))

racket_1 = Player("racket.png", 10, height/2-50, 7, (50,200))

racket_2 = Player("racket.png", width-35, height/2-50, 7, (50,200))

speed_x = 5
speed_y = 5
game_over = False
finish = False

while not game_over:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_over = True

    window.fill(background_color)
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.y > height-50 or ball.rect.y < 0:
        speed_y *= -1

    ball.reset()

    racket_1.reset()
    racket_2.reset()

    racket_1.update_l()
    racket_2.update_r()



    pygame.display.update()
    clock.tick(FPS)