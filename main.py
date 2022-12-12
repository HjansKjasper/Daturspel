import pygame as pg
from sprites import *
from random import randint

pg.init()

comic_sans30 = pg.font.SysFont("Comoc Sans MS", 100)

WHITE = (255,255,255)
BLACK = (0,0,0)
Fjarge = (20,37,110)
color = (100,100,100)

i = 0

WIDTH = 800

bg_img = pg.image.load("CrimeScene.jpg")


FPS = 120
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
friendly_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()

karakter = Player()
all_sprites.add(karakter)
friendly_group.add(karakter)

håkon = Player2()
all_sprites.add(håkon)
friendly_group.add(håkon)

politi = Police()
all_sprites.add(politi)
enemy_group.add(politi)

box_color = BLACK


screen = pg.display.set_mode((800,600))

playing = True 
while playing: # game loop
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

    screen.fill(Fjarge)

    
    screen.blit(bg_img,(i,0))
    screen.blit(bg_img,(WIDTH+i,0))
    if (i == -WIDTH):
        screen.blit(bg_img,(WIDTH+i,0))
        i=0
    i -=1

    all_sprites.update() 
 
    hits = pg.sprite.spritecollide(karakter, enemy_group, True)
    if hits: 
        karakter.health -= 10
        text_hp = comic_sans30.render("HP: " + str(karakter.health), False, color)
        if karakter.health <= 0:
            karakter.kill()
            hero = Player()
            all_sprites.add(hero)
    
    hits = pg.sprite.spritecollide(håkon, enemy_group, True)
    if hits: 
        håkon.health -= 10
        text_hp = comic_sans30.render("HP: " + str(håkon.health), False, color)
        if håkon.health <= 0:
            håkon.kill()
            hero = Player()
            all_sprites.add(hero)
    


    all_sprites.draw(screen)
  

    pg.display.update()