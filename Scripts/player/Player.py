from Orbital import Orbital
from Scripts.world.World import *
from Scripts.general.Constante import Constants


class Player:

    def __init__(self, name, color, rect):
        self.speed = 2
        self.health = 100
        self.damaged = False
        self.tick = 0
        self.current_room = 0

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

        display_rectangle = pygame.Rect(self.rect[0] - Constants.sX, self.rect[1] - Constants.sY, self.rect[2], self.rect[3])

        gameDisplay.fill(self.color, display_rectangle)

        if self.damaged:
            gameDisplay.fill((255, 0, 0, 100), display_rectangle)
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
                Constants.sX += self.speed
                Constants.send("coord|"+self.name+"|"+str(int(self.rect[0]))+","+str(int(self.rect[1]))+"|?")
            if Constants.A and not self.coliziune(-1, 0):
                self.rect[0] -= self.speed
                Constants.sX -= self.speed
                Constants.send("coord|"+self.name+"|"+str(int(self.rect[0]))+","+str(int(self.rect[1]))+"|?")
            if Constants.W and not self.coliziune(0, -1):
                self.rect[1] -= self.speed
                Constants.sY -= self.speed
                Constants.send("coord|"+self.name+"|"+str(int(self.rect[0]))+","+str(int(self.rect[1]))+"|?")
            if Constants.S and not self.coliziune(0, 1):
                self.rect[1] += self.speed
                Constants.sY += self.speed
                Constants.send("coord|"+self.name+"|"+str(int(self.rect[0]))+","+str(int(self.rect[1]))+"|?")

    def coliziune(self, dirX, dirY):
        col = False
        x = self.rect[0] / Constants.blockSize
        y = self.rect[1] / Constants.blockSize
        """
        for i in range(y-2, y+3):
            for j in range(x-2, x+3):
                if i >= 0 and j >= 0 and i < World.rooms[self.current_room].MAPHEIGHT and j < World.rooms[self.current_room].MAPWIDTH:
                    if pygame.Rect(self.rect[0] + dirX * self.speed, self.rect[1] + dirY * self.speed, self.rect[2], self.rect[3]).colliderect(World.rooms[self.current_room].map[i][j].rect)\
                       and World.rooms[self.current_room].map[i][j].type == 1:
                        col = True
        """
        return col
