import math

import pygame

from Scripts.general.Constante import Constants


class Orbital:

    angle = 180

    def __init__(self, playerName, width, height, imageName, damage, fireRate, distance, speed):
        self.playerName = playerName
        self.width = width
        self.height = height
        self.image = pygame.image.load("res/" + imageName + ".png");
        self.image = pygame.transform.scale(self.image, (width, height))
        self.damage = damage
        self.fireRate = fireRate
        self.distance = distance
        self.speed = speed

    def render(self, gameDisplay, playerRect):

        self.rect = pygame.Rect(float(playerRect[0] + playerRect[2] / 2 + math.cos(math.radians(self.angle)) * self.distance - self.width / 2),
                                float(playerRect[1] + playerRect[3] / 2 + math.sin(math.radians(self.angle)) * self.distance - self.height / 2), self.width, self.height)

        display_rectangle = pygame.Rect(self.rect[0] - Constants.sX, self.rect[1] - Constants.sY, self.rect[2], self.rect[3])

        self.changeAngle(-1, self.speed)

        if self.playerName == Constants.myId:
            if Constants.RIGHT:
                self.changeAngle(1, self.speed * 2)

        self.damageEnemies()
        gameDisplay.blit(self.image, display_rectangle)

    def changeAngle(self, modifier, amount):
            self.angle += modifier * amount
            if self.angle > 360:
                self.angle -= 360
            if self.angle < -360:
                self.angle += 360

    def damageEnemies(self):
        creatures = Constants.getMobs()

        for mob in creatures:
            if self.rect.colliderect(mob.rect):
                mob.damaged = True
                mob.health -= self.damage
            else:
                mob.damaged = False
