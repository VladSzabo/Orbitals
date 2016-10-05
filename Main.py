import pygame
from Player import Player
from StartMenu import StartMenu
from World import *
from Creatures import Creatures


class Main:

    gameDisplay = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT), pygame.DOUBLEBUF)
    clock = pygame.time.Clock()

    # Game Stuff
    startMenu = StartMenu()
    world = World()
    creatures = Creatures()
    player = Player(Constants.Colors["Green"], pygame.Rect(0., 0., Constants.WIDTH / 25, Constants.WIDTH / 25))

    def __init__(self):
        pygame.init()
        Constants()

        pygame.display.set_caption("Orbitals")
        self.startMenu.initFont()

    def mainLoop(self):
        while not Constants.gameExit:

            for event in pygame.event.get():
                self.handleKeys(event);

            self.render()
            self.update()

            self.clock.tick(60)

    def render(self):
        self.gameDisplay.fill(Constants.Colors["White"])

        if not Constants.firstMenu:
            self.world.render(self.gameDisplay)
            self.player.render(self.gameDisplay)
            self.creatures.render(self.gameDisplay)
        else:
            self.startMenu.render(self.gameDisplay)

        pygame.display.update()

    def update(self):
        if not Constants.firstMenu:
            self.player.update()
            self.creatures.update()
            if self.player.health < 0:
                Constants.gameOver = True
                print "Ai murit"

    def handleKeys(self, event):
        if event.type == pygame.QUIT:
            Constants.gameExit = True;
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Constants.A = True
            if event.key == pygame.K_w:
                Constants.W = True
            if event.key == pygame.K_s:
                Constants.S = True
            if event.key == pygame.K_d:
                Constants.D = True
            if event.key == pygame.K_LEFT:
                Constants.LEFT = True
            if event.key == pygame.K_RIGHT:
                Constants.RIGHT = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                Constants.A = False
            if event.key == pygame.K_w:
                Constants.W = False
            if event.key == pygame.K_s:
                Constants.S = False
            if event.key == pygame.K_d:
                Constants.D = False
            if event.key == pygame.K_LEFT:
                Constants.LEFT = False
            if event.key == pygame.K_RIGHT:
                Constants.RIGHT = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Constants.leftClick = True
            if event.button == 2:
                Constants.rightClick = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                Constants.leftClick = False
            if event.button == 3:
                Constants.rightClick = False

if __name__ == "__main__":
    Main().mainLoop()
    pygame.quit()
    quit()
