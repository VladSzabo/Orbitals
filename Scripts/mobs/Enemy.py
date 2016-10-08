import pygame

from Scripts.general.Constante import Constants
from Scripts.world.World import World

class Enemy:

    damaged = False

    def __init__(self, image, rect, damage, health, hitRate, speed, rangeInfo):
        self.rect = rect
        self.damage = damage
        self.hitRate = hitRate
        self.health = health
        self.speed = speed
        self.image = Constants.Mobs[image]
        self.image = pygame.transform.scale(self.image, (rect[2], rect[3]))

        if not(rangeInfo is None):
            self.ranged = True
            self.imageProjectile = pygame.image.load("res/mobs/" + rangeInfo[1] + ".png")
            self.imageProjectile = pygame.transform.scale(self.imageProjectile, (rangeInfo[2], rangeInfo[3]))
        else:
            self.ranged = False

    def render(self, gameDisplay):
        gameDisplay.blit(self.image, self.rect)
        if self.damaged:
            gameDisplay.fill((255, 0, 0, 0.1), self.rect)

    def update(self):
        self.update2()
        self.killPlayer()

    def killPlayer(self):
        players = Constants.getPlayers()
        for player in players:
            if self.rect.colliderect(player.rect):
                player.health -= self.damage
                player.damaged = True

    def update2(self):
        pass

    def move(self, dirX, dirY):
        dirY = -dirY
        if not self.coliziune(dirX, dirY):
            self.rect[0] += dirX * self.speed
            self.rect[1] += dirY * self.speed
            return True
        else:
            return False

    def coliziune(self, dirX, dirY):

        col = False
        x = int(self.rect[0] / Constants.blockSize)
        y = int(self.rect[1] / Constants.blockSize)

        for i in range(y-1, y+3):
            for j in range(x-2, x+2):
                if i >= 0 and j >= 0 and i < World.MAPHEIGHT and j < World.MAPWIDTH:
                    if pygame.Rect(self.rect[0] + dirX * self.speed, self.rect[1] + dirY * self.speed, self.rect[2], self.rect[3]).colliderect(World.map[i][j].rect)\
                       and World.map[i][j].type == 1:
                        col = True
                        break
            if col:
                break

        return col;