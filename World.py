import pygame
from random import randint
from Constante import Constants


class Block:

    def __init__(self, rect, spriteName, backgroundSpriteName, type, health):
        self.rect = rect
        self.spriteName = spriteName
        self.backgroundSpriteName = backgroundSpriteName
        self.type = type
        self.health = health

    def render(self, gameDisplay):
        if not(self.backgroundSpriteName is None):
            gameDisplay.blit(Constants.Images[self.backgroundSpriteName], self.rect)
        gameDisplay.blit(Constants.Images[self.spriteName], self.rect)

class World:

    def __init__(self):
        World.MAPWIDTH = 15
        World.MAPHEIGHT = 15
        World.map = []

        for i in range(World.MAPHEIGHT):
            World.map.append([])
            for j in range(World.MAPWIDTH):
                block = Block(pygame.Rect(j * Constants.blockSize, i * Constants.blockSize, Constants.blockSize,
                                            Constants.blockSize), "1", None, 0, 0)
                World.map[i].append(block)

        dark_blocks = randint(World.MAPWIDTH / 4, World.MAPWIDTH)
        for i in range(dark_blocks):
            x = randint(0, World.MAPWIDTH-1)
            y = randint(0, World.MAPHEIGHT-1)

            World.map[y][x] = Block(pygame.Rect(x * Constants.blockSize, y * Constants.blockSize, Constants.blockSize,
                                              Constants.blockSize), "2", "1", 1, 0)

    def render(self, gameDisplay):
        for i in range(World.MAPHEIGHT):
            for j in range(World.MAPWIDTH):
                World.map[i][j].render(gameDisplay)


