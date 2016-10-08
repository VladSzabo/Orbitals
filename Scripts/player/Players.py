import pygame

from Player import Player
from Scripts.general.Constante import Constants


class Players:

    players = []

    def __init__(self):
        Players.players.append(Player("P1", Constants.Colors["Green"], pygame.Rect(0., 0., Constants.WIDTH / 25, Constants.WIDTH / 25)))

    @staticmethod
    def render(gameDisplay):
        for player in Players.players:
            player.render(gameDisplay)

    @staticmethod
    def update():
        for player in Players.players:
            player.update()
            if player.health < 0:
                print "Player ", player.name, " a murit"
