import asyncore
import socket


class Server:

    clients = {}
    playersConnected = 0

    class MainServerSocket(asyncore.dispatcher):

        def __init__(self, port):
            asyncore.dispatcher.__init__(self)
            self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
            self.bind((socket.gethostname(), port))
            self.listen(5)

        def handle_accept(self):
            newSocket, address = self.accept()
            Server.clients[address] = newSocket
            print "Connected from", address
            Server.SecondaryServerSocket(newSocket)

    class SecondaryServerSocket(asyncore.dispatcher_with_send):

        def handle_read(self):
            receivedData = self.recv(8192)
            if receivedData:

                receivedData = str(receivedData)
                print "Server received: " + receivedData
                if "connect" in receivedData:
                    receivedData = receivedData + "|" + str(Server.playersConnected)
                    Server.playersConnected += 1

                every = Server.clients.values()
                for one in every:
                    one.send(receivedData)
            else:
                self.close()

        def handle_close(self):
            print "Disconnected from", self.getpeername()
            one = self.getpeername()
            Server.playersConnected -= 1
            del Server.clients[one]

    def __init__(self):
        pass

    @staticmethod
    def startServer():
        Server.MainServerSocket(21567)
        asyncore.loop()




