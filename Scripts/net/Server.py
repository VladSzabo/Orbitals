import socket


class Server:

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nrClients = 0
    clients = []

    def __init__(self):
        Server.serversocket.bind((socket.gethostname(), 8089))
        Server.serversocket.listen(5)
        print "Server Created"

    @staticmethod
    def ServerListen():
        while True:
            connection, address = Server.serversocket.accept()
            while True:
                buf = connection.recv(64)
                if len(buf) > 0:
                    if buf == "connect":
                        if not address in Server.clients:
                            Server.clients.append(address)
                            connection.sendto(("yourIdIs=" + str(Server.nrClients)).encode('utf-8'), address)
                            Server.nrClients += 1

                    print "Server received: " + str(buf) + " from: " + str(address)
                    break
                else:
                    break
            connection.close()
