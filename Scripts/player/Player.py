from Orbital import Orbital
from Scripts.world.World import *
from Scripts.general.Constante import Constants


class Player:

    speed = 2
    health = 100
    damaged = False
    tick = 0

    def __init__(self, name, color, rect):
        self.name = name
        self.color = color
        self.rect = rect
        self.rect[0] = Constants.WIDTH / 2 - self.rect[2] / 2
        self.rect[1] = Constants.HEIGHT / 2 - self.rect[3] / 2

        distance = rect[3] * 1.9
        self.orbitals = []
        self.orbitals.append(Orbital("", self.rect[2] / 2, self.rect[2] / 2, "orbital", 1, 1, distance, 2))
        # print(str(self.color) + " " + str(self.rect))

    def render(self, gameDisplay):

        gameDisplay.fill(self.color, self.rect)

        if self.damaged:
            gameDisplay.fill((255, 0, 0, 100), self.rect)
            self.tick += 1

            if self.tick > 10:
                self.damaged = False
                self.tick = 0

        for orb in self.orbitals:
            orb.render(gameDisplay, self.rect)

    def update(self):
        if self.name == Constants.myId:
            if Constants.D and not self.coliziune(1, 0):
                self.rect[0] += self.speed
                Constants.send("coord|"+self.name+"|"+str(int(self.rect[0]))+","+str(int(self.rect[1]))+","+str(int(self.rect[2]))+","+str(int(self.rect[3]))+"|")
            if Constants.A and not self.coliziune(-1, 0):
                self.rect[0] -= self.speed
                Constants.send("coord|"+self.name+"|"+str(int(self.rect[0]))+","+str(int(self.rect[1]))+","+str(int(self.rect[2]))+","+str(int(self.rect[3]))+"|")
            if Constants.W and not self.coliziune(0, -1):
                self.rect[1] -= self.speed
                Constants.send("coord|"+self.name+"|"+str(int(self.rect[0]))+","+str(int(self.rect[1]))+","+str(int(self.rect[2]))+","+str(int(self.rect[3]))+"|")
            if Constants.S and not self.coliziune(0, 1):
                self.rect[1] += self.speed
                Constants.send("coord|"+self.name+"|"+str(int(self.rect[0]))+","+str(int(self.rect[1]))+","+str(int(self.rect[2]))+","+str(int(self.rect[3]))+"|")

    def coliziune(self, dirX, dirY):
        col = False
        x = self.rect[0] / Constants.blockSize
        y = self.rect[1] / Constants.blockSize

        for i in range(y-2, y+3):
            for j in range(x-2, x+3):
                if i >= 0 and j >= 0 and i < World.MAPHEIGHT and j < World.MAPWIDTH:
                    if pygame.Rect(self.rect[0] + dirX * self.speed, self.rect[1] + dirY * self.speed, self.rect[2], self.rect[3]).colliderect(World.map[i][j].rect)\
                       and World.map[i][j].type == 1:
                        col = True
        return col
