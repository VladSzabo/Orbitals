from socket import *
from Scripts.player.Players import Players
from Scripts.general.Constante import Constants
from threading import Thread


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
                Client.firstTimeConnect = True
                id = data.split("|")[1]

                Constants.myId = id
                Players.players[0].name = id
                if int(id) >= 1:
                    for i in range(int(id)):
                        Players.addPlayer(i)
            else:
                Players.addPlayer(Client.playersConnected)
                Client.playersConnected += 1

