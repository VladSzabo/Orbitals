from __future__ import print_function
import pygame
from Scripts.general.Constante import Constants


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


class Room:

    def __init__(self, file_name, x_big, y_big):
        self.x_big = x_big
        self.y_big = y_big
        self.file_name = file_name
        self.MAPHEIGHT = 10
        self.MAPWIDTH = 10
        self.map = []

        file_map = open("maps/" + file_name)

        sizes = file_map.readline().split(" ")
        self.MAPHEIGHT = int(sizes[0])
        self.MAPWIDTH = int(sizes[1])

        y = 0
        for line in file_map.readlines():
            self.map.append([])
            values = line.split(" ")
            x = -1

            for value in values:
                x += 1
                try:
                    value = int(value)

                    if value % 2 == 0:
                        type1 = True
                    else:
                        type1 = False

                    self.map[y].append(Block(pygame.Rect((self.x_big-2500) * Constants.blockSize + x/2 * Constants.blockSize, (self.y_big-2500) * Constants.blockSize + y * Constants.blockSize,
                                                         Constants.blockSize, Constants.blockSize),
                                       str(value), None, type1, 100))
                except ValueError:
                    pass
            y += 1

    def render(self, gameDisplay):
        for i in range(self.MAPHEIGHT):
            for j in range(self.MAPWIDTH):
                self.map[i][j].render(gameDisplay)