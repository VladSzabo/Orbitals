from socket import *
from Scripts.player.Players import Players
from Scripts.general.Constante import Constants
from threading import Thread
import pygame


class Client:

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    playersConnected = 1
    firstTimeConnect = True

    def __init__(self, ip):
        Client.tcpCliSock.connect((ip, 21567))
        print "Client connected to IP: " + str(ip)

    @staticmethod
    def send(message):
        Client.tcpCliSock.send(message)

    @staticmethod
    def socket():
        def loop0():
            while 1:
                data = Client.tcpCliSock.recv(1024)
                if data:
                    print "Client Received: " + str(data)
                    Client.interpreteazaData(data)

        thread = Thread(target = loop0)
        thread.start()

    @staticmethod
    def StartClient():
        Client.socket()
        Client.send("connect")

    @staticmethod
    def interpreteazaData(data):
        data = str(data)
        if "connect" in data:
            if Client.firstTimeConnect:
                Client.firstTimeConnect = False
                id = data.split("|")[1]
                Client.playersConnected = int(id) + 1

                Constants.myId = id
                Players.players[0].name = id
                Players.players[0].orbitals[0].playerName = id
                if int(id) >= 1:
                    for i in range(int(id)):
                        Players.addPlayer(i)
            else:
                Players.addPlayer(Client.playersConnected)
                Client.playersConnected += 1
        else:
            if "coord" in data:
                data = data.split("|")
                if data[1] != Constants.myId:
                    coords = data[2].split(",")
                    for player in Players.players:
                        if player.name == data[1]:
                            try:
                                player.rect = pygame.Rect(int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]))
                            finally:
                                break

