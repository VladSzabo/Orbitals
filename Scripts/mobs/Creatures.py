import math
from random import randint
from types import MethodType

import pygame

from Enemy import Enemy
from Scripts.general.Constante import Constants
from Scripts.world.World import World

class Creatures:

    def __init__(self):
        pass

    @staticmethod
    def generareMobs():
        Creatures.mobs = []

        def zombieUpdate(self):
            # Follow Player
            players = Constants.getPlayers()
            closerPlayerId = 0
            smallestDistance = 2 ** 14
            id = 0

            for player in players:
                distance = Constants.distanta(self.rect, player.rect)
                if distance < smallestDistance:
                    smallestDistance = distance
                    closerPlayerId = id
                id += 1

            angle = Constants.getAngle(self.rect[0], self.rect[1], players[closerPlayerId].rect[0],
                                       players[closerPlayerId].rect[1])
            canMove = self.move(math.cos(math.radians(angle)), math.sin(math.radians(angle)))

            if not canMove:
                if math.fabs(self.rect[0] - players[closerPlayerId].rect[0]) > math.fabs(
                                self.rect[1] - players[closerPlayerId].rect[1]):
                    if math.sin(math.radians(angle)) >= 0:
                        self.move(0, 1.)
                    else:
                        self.move(0, -1.)
                else:
                    if math.cos(math.radians(angle)) >= 0:
                        self.move(1., 0)
                    else:
                        self.move(-1., 0)

        nrZombies = 1

        for i in range(nrZombies):
            x = randint(0, Constants.WIDTH)
            y = randint(0, Constants.HEIGHT)

            Zombie = Enemy("Zombie", pygame.Rect(x, y, Constants.WIDTH / 24, Constants.WIDTH / 12), 1, 100, 1, 2, None)
            Zombie.update2 = MethodType(zombieUpdate, Zombie)

            Creatures.mobs.append(Zombie)

    @staticmethod
    def render(gameDisplay):
        for mob in Creatures.mobs:
            mob.render(gameDisplay)

    @staticmethod
    def update():
        for i in range(len(Creatures.mobs)):
            if i < len(Creatures.mobs):
                Creatures.mobs[i].update()
                if Creatures.mobs[i].health <= 0:
                    Creatures.mobs.pop(i)

        if len(Creatures.mobs) == 0:
            # World.generateWorld()
            Creatures.generareMobs()

