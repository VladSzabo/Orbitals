import pygame
import math


class Constants:

    Colors = {
        "Red": (255, 0, 0),
        "Black": (0, 0, 0),
        "White": (255, 255, 255),
        "Green": (0, 255, 0),
        "Blue": (0, 0, 255)
    }
    Images = {
        "1": pygame.image.load("res/1.png"),
        "2": pygame.image.load("res/2.png"),
        "3": pygame.image.load("res/3.png"),
    }
    Mobs = {
        "Zombie": pygame.image.load("res/mobs/zombie.png")
    }

    A, W, S, D = False, False, False, False
    leftClick, rightClick = False, False
    LEFT, RIGHT = False, False

    WIDTH = 800
    HEIGHT = 600
    gameExit = False
    gameOver = False
    firstMenu = True
    blockSize = WIDTH / 15

    def __init__(self):
        for i in range(len(self.Images)):
            self.Images[str(i+1)] = pygame.transform.scale(self.Images[str(i+1)], (self.blockSize, self.blockSize))

    @staticmethod
    def getAngle(x1, y1, x2, y2):

        dx = x2 - x1
        dy = y2 - y1
        return math.degrees(math.atan2(dx, dy)) - 90

    @staticmethod
    def getMobs():
        from Creatures import Creatures
        return Creatures.mobs