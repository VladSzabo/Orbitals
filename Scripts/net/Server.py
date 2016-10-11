import asyncore
import socket


class Server:

    clients = {}
    clientsId = {}
    playersConnected = -1

    class MainServerSocket(asyncore.dispatcher):

        def __init__(self, port):
            asyncore.dispatcher.__init__(self)
            self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
            self.bind((socket.gethostname(), port))
            self.listen(5)

        def handle_accept(self):
            newSocket, address = self.accept()
            Server.clients[address] = newSocket
            Server.playersConnected += 1
            Server.clientsId[address] = Server.playersConnected

            print "Connected from", address
            Server.SecondaryServerSocket(newSocket)

    class SecondaryServerSocket(asyncore.dispatcher_with_send):

        def handle_read(self):
            receivedData = self.recv(8192)
            if receivedData:

                receivedData = str(receivedData)
                print "Server received: " + receivedData

                player = None
                if "|" in str(receivedData):
                    player = str(receivedData).split("|")
                    player = player[1]

                if "connect" in receivedData:
                    receivedData = receivedData + "|" + str(Server.playersConnected)

                for key in Server.clients:
                    if player is None:
                        Server.clients[key].send(receivedData)
                    elif Server.clientsId[key] != int(player):
                        Server.clients[key].send(receivedData)
            else:
                self.close()

        def handle_close(self):
            print "Disconnected from", self.getpeername()
            one = self.getpeername()
            Server.playersConnected -= 1
            del Server.clients[one]
            del Server.clientsId[one]

    def __init__(self):
        pass

    @staticmethod
    def startServer():
        Server.MainServerSocket(21567)
        asyncore.loop()




