from Enemy import Enemy
from Constante import Constants
import pygame
from types import MethodType
from Player import Player
import math
from random import randint
import copy

class Creatures:

    def __init__(self):
        Creatures.mobs = []

        def zombieUpdate(self):
            # Follow Player
            angle = Constants.getAngle(self.rect[0], self.rect[1], Player.rect[0], Player.rect[1])
            self.rect[0] += math.cos(math.radians(angle)) * self.speed
            self.rect[1] -= math.sin(math.radians(angle)) * self.speed

        nrZombies = 3

        for i in range(nrZombies):
            x = randint(0, Constants.WIDTH)
            y = randint(0, Constants.HEIGHT)

            Zombie = Enemy("Zombie", pygame.Rect(x, y, Constants.WIDTH / 24, Constants.WIDTH / 12), 1, 100, 1, 2, None)
            Zombie.update2 = MethodType(zombieUpdate, Zombie)

            Creatures.mobs.append(Zombie)

    def render(self, gameDisplay):
        for mob in Creatures.mobs:
            mob.render(gameDisplay)

    def update(self):
        for i in range(len(Creatures.mobs)):
            if i < len(Creatures.mobs):
                Creatures.mobs[i].update()
                if Creatures.mobs[i].health <= 0:
                    Creatures.mobs.pop(i)


