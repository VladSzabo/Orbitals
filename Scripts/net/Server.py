import socket
import threading


class Server:

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nrClients = 0
    clients = []
    clients_lock = threading.Lock()

    def __init__(self):
        Server.serversocket.bind((socket.gethostname(), 8089))
        Server.serversocket.listen(5)
        print "Server Created"

    @staticmethod
    def ServerListen():
        while True:
            connection, address = Server.serversocket.accept()
            with Server.clients_lock:
                Server.clients.append(connection)
                connection.sendall("yourIdIs=" + str(Server.nrClients))
                Server.nrClients += 1
            try:
                while True:
                    buf = connection.recv(64)
                    if len(buf) > 0:
                        print "Server received: " + str(buf) + " from: " + str(address)
                        with Server.clients_lock:
                            for c in Server.clients:
                                c.sendall(buf)
                        break
                    else:
                        break
            finally:
                pass