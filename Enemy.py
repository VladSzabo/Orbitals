import pygame
import random
from Constante import Constants
from Player import Player

class Enemy:

    damaged = False

    def __init__(self, image, rect, damage, health, hitRate, speed, rangeInfo):
        self.rect = rect
        self.damage = damage
        self.hitRate = hitRate
        self.health = health
        self.speed = speed
        self.image = Constants.Mobs[image]
        self.image = pygame.transform.scale(self.image, (rect[2], rect[3]))

        if not(rangeInfo is None):
            self.ranged = True
            self.imageProjectile = pygame.image.load("res/mobs/" + rangeInfo[1] + ".png")
            self.imageProjectile = pygame.transform.scale(self.imageProjectile, (rangeInfo[2], rangeInfo[3]))
        else:
            self.ranged = False

    def render(self, gameDisplay):
        gameDisplay.blit(self.image, self.rect)
        if self.damaged:
            gameDisplay.fill((255, 0, 0, 0.1), self.rect)

    def update(self):
        self.update2()
        self.killPlayer()

    def killPlayer(self):
        if self.rect.colliderect(Player.rect):
            Player.health -= self.damage
            Player.damaged = True


    def update2(self):
        pass
