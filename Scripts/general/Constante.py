import math
import pygame


class Constants:

    myId = '0'

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
        "4": pygame.image.load("res/4.png")
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
    blockSize = WIDTH / 70
    # Scroll
    sX = 0
    sY = 0

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
        from Scripts.mobs.Creatures import Creatures
        return Creatures.mobs

    @staticmethod
    def getPlayers():
        from Scripts.player.Players import Players
        return Players.players

    @staticmethod
    def distanta(rect1, rect2):
        return math.sqrt((rect1[0]-rect2[0])**2.+(rect1[1]-rect2[1])**2.)

    @staticmethod
    def getMapSource():
        from Scripts.general.Main import Main
        return Main.world

    @staticmethod
    def initClient(ip):
        from Scripts.net.Client import Client
        Client(ip)
        Client.StartClient()

    @staticmethod
    def initServer():
        from threading import Thread
        from Scripts.net.Server import Server
        thread = Thread(target = Server.startServer)
        thread.start()

    @staticmethod
    def send(message):
        from Scripts.net.Client import Client
        Client.send(message)
