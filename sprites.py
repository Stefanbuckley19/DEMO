# sprite classes for game

import pygame as pg
from pygame.sprite import Sprite
import random
from setting import *

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.vx = 0
        self.vy = 0
        self.acceleration = .5
        self.falling = False
        self.max_velocity = -25
    def update(self):
        self.vx = 0
        # self.vy = 0 
        self.gravity()
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -5
        if keys[pg.K_RIGHT]:
            self.vx = 5
        if keys[pg.K_UP] and self.falling == False:
            self.jump()
        self.rect.x += self.vx
        self.rect.y += self.vy
    def gravity(self):
        if self.rect.y <= HEIGHT-40:
            self.falling = True
            print("gravity is happening! " + str(self.rect.y))
            print("falling " + str(self.falling))
            self.vy += 10
        else:
                self.falling = False
                self.vy = 0
                print("falling " + str(self.falling))
    def jump(self):
        self.vy = -75
        print("jump called ")



