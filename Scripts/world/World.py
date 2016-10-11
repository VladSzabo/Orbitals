from random import randint

import pygame

from Scripts.general.Constante import Constants
from Scripts.world.Room import Room

class Block:

    def __init__(self, rect, spriteName, backgroundSpriteName, type, health):
        self.rect = rect
        self.spriteName = spriteName
        self.backgroundSpriteName = backgroundSpriteName
        self.type = type
        self.health = health

    def render(self, gameDisplay):

        display_rectangle = pygame.Rect(self.rect[0] - Constants.sX, self.rect[1] - Constants.sY, self.rect[2], self.rect[3])

        if not(self.backgroundSpriteName is None):
            gameDisplay.blit(Constants.Images[self.backgroundSpriteName], display_rectangle)
        gameDisplay.blit(Constants.Images[self.spriteName], display_rectangle)


class World:

    rooms = []

    def __init__(self):
        pass

    @staticmethod
    def generateWorld():
        World.rooms.append(Room("1"))

    @staticmethod
    def render(gameDisplay):

        for room in World.rooms:
            room.render(gameDisplay)



