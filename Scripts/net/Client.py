import socket


class Client:

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, ip):
        Client.clientsocket.connect((ip, 8089))
        print "Client connected to IP: " + str(ip)

    @staticmethod
    def sendInfo(message):
        Client.clientsocket.send(message)

    @staticmethod
    def ClientListen():
        while True:
            data = Client.clientsocket.recv(64)
            if len(data)> 0:
                print ""
                print "Client Received: " + str(data)