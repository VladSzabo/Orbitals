import socket
from Scripts.player.Players import Players
from Scripts.general.Constante import Constants

class Client:

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    playersConnected = 0

    def __init__(self, ip):
        Client.clientsocket.connect((ip, 8089))
        print "Client connected to IP: " + str(ip)

    @staticmethod
    def sendInfo(message):
        Client.clientsocket.send(message)

    """
        AMINTIRE!!!

        Inca nu am implementat suport pentru mai mult de 2 playeri

    """

    @staticmethod
    def ClientListen():
        while True:
            data = Client.clientsocket.recv(64)
            if len(data)> 0:
                if "yourIdIs=" in str(data):
                    Constants.myId = (str(data).split('='))[1]
                    Players.players[0].name = Constants.myId
                    for orb in Players.players[0].orbitals:
                        orb.playerName = Constants.myId

                    if Constants.myId == '1':
                        Players.addPlayer(0)

                if "connect" in str(data):
                    Client.playersConnected += 1
                    if Client.playersConnected == 2:
                        Players.addPlayer(1)
                print ""
                print "Client Received: " + str(data)