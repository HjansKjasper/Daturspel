import pygame as pg
from sprites import *
from random import randint
from pygame import mixer


class Game():
    def __init__(self): # kode når vi starter spillet

        self.screen = pg.display.set_mode((800,600))

        pg.init()
 
        self.comic_sans30 = pg.font.SysFont("Comoc Sans MS", 100)

        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.Fjarge = (20,37,110)
        self.color = (220,210,0)

        self.i = 0

        self.WIDTH = 800

        self.bg_img = pg.image.load("CrimeScene.jpg")


        self.FPS = 120
        self.clock = pg.time.Clock()

        pg.mixer.music

        self.new()

    

    def new(self): # kode som trengs for en ny runde

        self.all_sprites = pg.sprite.Group()
        self.friendly_group = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()

        self.karakter = Player(self)
        self.all_sprites.add(self.karakter)
        self.friendly_group.add(self.karakter)

        self.håkon = Player2(self)
        self.all_sprites.add(self.håkon)
        self.friendly_group.add(self.håkon)

        self.politi = Police()
        self.all_sprites.add(self.politi)
        self.enemy_group.add(self.politi)

        self.box_color = self.BLACK

        self.text_hp = self.comic_sans30.render("HP: " + str(self.karakter.health), False, self.color)



        self.run()

    def run(self):

        #self.screen.blit
        
        playing = True 
        while playing: # game loop
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing = False

            self.screen.fill(self.Fjarge)

            
            self.screen.blit(self.bg_img,(self.i,0))
            self.screen.blit(self.bg_img,(self.WIDTH+self.i,0))
            if (self.i == -self.WIDTH):
                self.screen.blit(self.bg_img,(self.WIDTH+self.i,0))
                self.i=0
            self.i -=1

            self.all_sprites.update() 
    
            hits = pg.sprite.spritecollide(self.karakter, self.enemy_group, True)
            if hits: 
                self.karakter.health -= 10
                self.text_hp = self.comic_sans30.render("HP: " + str(self.karakter.health), False, self.color)
                if self.karakter.health <= 0:
                    self.karakter.kill()
                    hero = Player()
                    self.all_sprites.add(hero)
            
            hits = pg.sprite.spritecollide(self.håkon, self.enemy_group, True)
            if hits: 
                self.håkon.health -= 10
                self.text_hp = self.comic_sans30.render("HP: " + str(self.håkon.health), False, self.color)
                if self.håkon.health <= 0:
                    self.håkon.kill()
                    hero = Player()
                    self.all_sprites.add(hero)

            
            if len(self.enemy_group) < 1:
                self.politi = Police()
                self.all_sprites.add(self.politi)
                self.enemy_group.add(self.politi)

            
        
        
            self.all_sprites.draw(self.screen)

            self.screen.blit(self.text_hp,(10,10))
        

            pg.display.update()


g = Game()
