import pygame

from Scripts.general.Constante import Constants
import inputbox

class StartMenu:

    def __init__(self):
        pass

    def initFont(self):
        self.initOrbitalFont(Constants.HEIGHT / 9)

        self.fontStart = pygame.font.Font("res/menufont.ttf", Constants.HEIGHT / 14)
        # self.fontStart.set_bold(True)
        self.connectSize = self.fontStart.size("CONNECT")
        self.connectText = self.fontStart.render("CONNECT", True, Constants.Colors["Red"])
        self.serverSize = self.fontStart.size("CREATE SERVER")
        self.serverText = self.fontStart.render("CREATE SERVER", True, Constants.Colors["Red"])

    def initOrbitalFont(self, size):
        self.fontOrbitals = pygame.font.Font("res/menufont.ttf", size)
        self.fontOrbitals.set_bold(True)
        self.orbitalsSize = self.fontOrbitals.size("Orbitals")
        self.orbitalsText = self.fontOrbitals.render("Orbitals", True, Constants.Colors["Blue"])

    sizeChange = 0
    increasing = False
    timer = 0
    connectToServer = False
    inp = None

    def render(self, gameDisplay):
        gameDisplay.blit(self.orbitalsText, [Constants.WIDTH / 2 - self.orbitalsSize[0] / 2, Constants.HEIGHT / 4 - self.orbitalsSize[1] / 2])


        if not self.connectToServer:
            gameDisplay.blit(self.connectText, [Constants.WIDTH / 2 - self.connectSize[0] / 2, Constants.HEIGHT / 1.8 - self.connectSize[1] / 2])
            gameDisplay.blit(self.serverText, [Constants.WIDTH / 2 - self.serverSize[0] / 2, Constants.HEIGHT / 1.4 - self.serverSize[1] / 2])
            mpos = pygame.mouse.get_pos()
            if Constants.leftClick and pygame.Rect(Constants.WIDTH / 2 - self.connectSize[0] / 2,
                                                   Constants.HEIGHT / 1.8 - self.connectSize[1] / 2,
                                                   self.connectSize[0], self.connectSize[1]).collidepoint(mpos):
                self.connectToServer = True

            if Constants.leftClick and pygame.Rect(Constants.WIDTH / 2 - self.serverSize[0] / 2,
                                                   Constants.HEIGHT / 1.4 - self.serverSize[1] / 2, self.serverSize[0],
                                                   self.serverSize[1]).collidepoint(mpos):
                Constants.firstMenu = False
                Constants.initServer()
                Constants.initClient('localhost')
        else:
            if self.inp is None:
                self.inp = inputbox.ask(gameDisplay, 'IP')
            else:
                Constants.initClient(self.inp)


        if self.timer % 3 == 0:
            if self.increasing:
                if self.sizeChange < 6:
                    self.sizeChange += 1
                else:
                    self.increasing = False
                self.initOrbitalFont(Constants.HEIGHT / 9 + self.sizeChange)
            else:
                if self.sizeChange > -6:
                    self.sizeChange -= 1
                else:
                    self.increasing = True
                self.initOrbitalFont(Constants.HEIGHT / 9 + self.sizeChange)

        self.timer += 1
        if self.timer > 1004:
            self.timer = 0