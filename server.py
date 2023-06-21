import socket
from threading import Thread

class ClientNode:
    # recieves data from clients

    def __init__(self, client_socket, connection_manager):
        self.client_socket = client_socket
        self.user_name = ''
        self.connection_manager = connection_manager
        self.run_threads = True

    def start_recieve_thread(self):
        self.recieve_thread = Thread(target=self.recieve_messages)
        self.recieve_thread.start()

    def assign_user_name_thread(self):
        self.user_name_thread = Thread(target=self.assign_user_name)
        self.user_name_thread.start()

    def assign_user_name(self):
        try:
            data = self.client_socket.recv(1024)
            self.user_name = data.decode("UTF-8")
            self.connection_manager.send_all(self.user_name + " joined the chat", self)
        except Exception as e:
            print(e)
            self.connection_manager.destroy_client(self)

    def recieve_messages(self):
        while self.run_threads:
            client_message = self.client_socket.recv(1024)
            if not client_message:
                self.connection_manager.send_all(self.user_name + " left the chat", self)
                self.connection_manager.destroy_client(self)
                return
            client_message = client_message.decode("UTF-8")
            self.connection_manager.send_all(self.user_name + ": " + client_message, self)

                     
    def send_message(self, message):
        self.client_socket.send(bytes(message, "UTF-8"))


class ConnectionMannager:
    # listens for new clients and then assigns them nodes
    # also sends to all clients

    def __init__(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def bind_socket(self, IP, PORT):
        try:
            self.socket.bind((IP, PORT))
        except:
            print("Address Taken")

    def create_client(self, client_socket):
        client = ClientNode(client_socket, self)
        self.clients.append(client)
        client.assign_user_name_thread()
        client.start_recieve_thread()


    
    def socket_listen(self):
        # Probobly Need to Thread this!!!!!!!
        while True:
            self.socket.listen(1)
            client_socket, _ = self.socket.accept()
            self.create_client(client_socket)
            # self.send_all("message")
            # print(client.user_name)
            print(self.clients)

    def destroy_client(self, object):
        len_clients = len(self.clients)
        for index in range(len_clients):
            if self.clients[index] == object:
                # print(f'USER: {self.clients[index]} Removed')
                self.clients[index].run_threads = False
                del self.clients[index]

    def send_all(self, message, current_client):
        for client in self.clients:
            if client != current_client:
                client.send_message(message)


def main():
    server = ConnectionMannager()
    server.bind_socket("0.0.0.0", 12345)
    try:
        server.socket_listen()
    finally:
        server.socket.close()
        for client in server.clients:
            client.client_socket.close()




if __name__ == "__main__":
    main()
    # server = ConnectionMannager()
    # server.bind_socket("0.0.0.0", 12345)
    # try:
    #     server.socket_listen()
    # finally:
    #     for client in server.clients:
    #         client.client_socket.close()
    #     server.socket.close()