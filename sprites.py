import pygame as pg
from pygame import image
vec = pg.math.Vector2
from random import randint


enemy_image = pg.image.load("monk.png")
player_image = pg.image.load("ninja weapon.png")
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_image 
        self.image = pg.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.pos = vec(500, 0)
        self.rect.center = self.pos
        self.speed = 5
        self.kills = 0
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= self.speed
        if keys[pg.K_a]:
            self.pos.x -= self.speed
        if keys[pg.K_d]:
            self.pos.x += self.speed
        if keys[pg.K_s]:
            self.pos.y += self.speed 

        self.rect.center = self.pos

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.image = pg.transform.scale(self.image, (100,100)) 
        self.rect = self.image.get_rect()
        self.pos = vec(0, 500)
        self.rect.center = self.pos
        self.speed_x = 1
        
    def update(self):
        self.pos.x += self.speed_x
        if self.pos.x > 800: #hvis til høyre for skjerm
            self.speed_x = -1
        if self.pos.x < 0: #hvis til venstre for skjerm
            self.speed_x = 1
        self.rect.center = self.pos

class Attacke(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = "shuriken.png"
        self.rect = self.image.get_rect()
        self.pos = vec(randint(0,0), randint (0,600))
        self.speed_x = 2

  
       