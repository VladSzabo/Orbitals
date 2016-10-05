import pygame
from World import *
from Orbital import Orbital


class Player:

    speed = 2
    health = 100
    nrOfOrbitals = 1
    orbitals = []
    damaged = False
    tick = 0

    def __init__(self, color, rect):
        Player.color = color;
        Player.rect = rect;
        Player.rect[0] = Constants.WIDTH / 2 - Player.rect[2] / 2
        Player.rect[1] = Constants.HEIGHT / 2 - Player.rect[3] / 2

        distance = rect[3] * 1.9
        Player.orbitals.append(Orbital(Player.rect[2] / 2, Player.rect[2] / 2, "orbital", 1, 1, distance, 2))

        # print(str(Player.color) + " " + str(Player.rect))

    def render(self, gameDisplay):

        gameDisplay.fill(Player.color, self.rect)

        if Player.damaged:
            gameDisplay.fill((255, 0, 0, 100), self.rect)
            Player.tick += 1

            if Player.tick > 10:
                Player.damaged = False
                Player.tick = 0


        for orb in Player.orbitals:
            orb.render(gameDisplay, Player.rect)

    def update(self):
        if Constants.D and not self.coliziune(1, 0):
            Player.rect[0] += Player.speed
        if Constants.A and not self.coliziune(-1, 0):
            Player.rect[0] -= Player.speed
        if Constants.W and not self.coliziune(0, -1):
            Player.rect[1] -= Player.speed
        if Constants.S and not self.coliziune(0, 1):
            Player.rect[1] += Player.speed

    def coliziune(self, dirX, dirY):
        col = False
        x = Player.rect[0] / Constants.blockSize
        y = Player.rect[1] / Constants.blockSize

        for i in range(y-2, y+3):
            for j in range(x-2, x+3):
                if i >= 0 and j >= 0 and i < World.MAPHEIGHT and j < World.MAPWIDTH:
                    if pygame.Rect(Player.rect[0] + dirX * Player.speed, Player.rect[1] + dirY * Player.speed, Player.rect[2], Player.rect[3]).colliderect(World.map[i][j].rect)\
                       and World.map[i][j].type == 1:
                        col = True
        return col
