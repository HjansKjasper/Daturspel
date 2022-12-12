import pygame as pg
from random import randint 
vec = pg.math.Vector2

player_img = pg.image.load("H.jpg")
player_img = pg.transform.scale(player_img,(130,100))
håkon_img = pg.image.load("Håkon.png")
håkon_img = pg.transform.scale(håkon_img,(300,100))
police_img = pg.image.load("Nat.png")
police_img = pg.transform.scale(police_img,(130,100))

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self) #Mamma Mø
        self.game = game
        self.image = player_img
        self.rect = self.image.get_rect()
        self.pos = vec(100,100)
        self.rect.center =self.pos
        self.speed = 3
        self.health = 100

    def update(self):
        self.rect.center = self.pos

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= self.speed
        if keys[pg.K_s]:
            self.pos.y += self.speed
        if keys[pg.K_a]:
            self.pos.x -= self.speed
        if keys[pg.K_d]:
            self.pos.x += self.speed 

class Player2(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self) #Mamma Mø

        self.game = game
        self.image = håkon_img
        self.rect = self.image.get_rect()
        self.pos = vec(600,100)
        self.rect.center =self.pos
        self.speed = 3
        self.health = 100


    def update(self):
        self.rect.center = self.pos

        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.pos.y -= self.speed
        if keys[pg.K_DOWN]:
            self.pos.y += self.speed
        if keys[pg.K_LEFT]:
            self.pos.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.pos.x += self.speed 

class Police(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self) #Mamma Mø

        self.image = police_img
        self.rect = self.image.get_rect()
        self.pos = vec(randint(100,600), randint(300,550))
        self.rect.center =self.pos
        self.speed = 3

    def update(self):
        self.rect.center = self.pos

        