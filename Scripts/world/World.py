from random import randint

import pygame
from os import listdir
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
    def generateWorld(nr_of_rooms = 15):
        maps = listdir("maps")

        map_size = 5000
        map_check = [[0 for i in range(map_size)] for i in range(map_size)]

        for i in range(nr_of_rooms):
            map = maps[randint(0, len(maps) - 1)]
            x = map_size / 2
            y = map_size / 2

            my_room = Room(map, 0, 0)

            if i > 0:

                connection_points = []

                for room in World.rooms:
                    # LEFT
                    for j in range(room.y_big+1, room.y_big + room.MAPHEIGHT-1):
                        if map_check[j][room.x_big] == 0:
                            connection_points.append([j, room.x_big, "left"])
                    # TOP
                    for j in range(room.x_big+1, room.x_big + room.MAPWIDTH-1):
                        if map_check[room.y_big][j] == 0:
                            connection_points.append([room.y_big, j, "top"])
                    # RIGHT
                    for j in range(room.y_big+1, room.y_big + room.MAPHEIGHT-1):
                        if map_check[j][room.x_big+room.MAPWIDTH] == 0:
                            connection_points.append([j, room.x_big+room.MAPWIDTH, "right"])
                    # DOWN
                    for j in range(room.x_big+1, room.x_big + room.MAPWIDTH-1):
                        if map_check[room.y_big+room.MAPHEIGHT][j] == 0:
                            connection_points.append([room.y_big+room.MAPHEIGHT, j, "down"])

                found = False
                while not found:
                    connection_id = randint(0, len(connection_points) - 1)

                    x_cp = None
                    y_cp = None

                    if connection_points[connection_id][2] == "left":
                        y_cp = connection_points[connection_id][0] - my_room.MAPHEIGHT
                        x_cp = connection_points[connection_id][1] - my_room.MAPWIDTH
                    if connection_points[connection_id][2] == "top":
                        y_cp = connection_points[connection_id][0] - my_room.MAPHEIGHT
                        x_cp = connection_points[connection_id][1]
                    if connection_points[connection_id][2] == "right" or connection_points[connection_id][2] == "down":
                        y_cp = connection_points[connection_id][0]
                        x_cp = connection_points[connection_id][1]

                    col = False
                    for room in World.rooms:
                        if pygame.Rect(x_cp, y_cp, my_room.MAPWIDTH, my_room.MAPHEIGHT).colliderect(pygame.Rect(room.x_big, room.y_big, room.MAPWIDTH, room.MAPHEIGHT)):
                            col = True
                            break

                    if col:
                        connection_points.pop(connection_id)
                    else:
                        x = x_cp
                        y = y_cp
                        found = True

            World.rooms.append(Room(map, x, y))

            current = World.rooms[len(World.rooms)-1]
            for m in range(current.y_big, current.y_big + current.MAPHEIGHT):
                for n in range(current.x_big, current.x_big + current.MAPWIDTH):
                    map_check[m][n] = 1

            del my_room

        for room in World.rooms:
            print room.MAPWIDTH, room.MAPHEIGHT, room.x_big, room.y_big

        del map_check

    @staticmethod
    def render(gameDisplay):

        for room in World.rooms:
            room.render(gameDisplay)
