import socket
from threading import Thread


class ClientBackend:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def connect_to_server(self, IP, PORT):
        self.socket.connect((IP, PORT))
        self.send_user_name()
    
    def assign_user_name(self):
        # this takes the user name before we send it to the server
        # prediction: front end thing
        self.user_name = input("username: ")

    def send_user_name(self) -> str:
        # sends username to server
        # user_name = input() # will get username from file
        self.send_message(self.user_name)
    
    def send_message(self, text):
        # takes in string
        self.socket.send(bytes(text,"UTF-8"))

    def input_message(self) -> str:
        return input("")
    
    def start_recieve_thread(self):
        self.recieve_thread = Thread(target=self.recieve_messages)
        self.recieve_thread.start()

    def recieve_messages(self):
        while True:
            try:
                data = self.socket.recv(1024)
                if not data:
                    print("Disconnected from server")
                    return
                print(data.decode("UTF-8"))
            except:
                print("Disconnected from server: error")
                return

    def start_input_loop(self):
        try:
            while True:
                message = self.input_message()
                self.send_message(message)
        finally:
            self.socket.close()

user = ClientBackend()
user.assign_user_name()
user.connect_to_server("10.0.0.125", 12345)
user.start_recieve_thread()
user.start_input_loop()


# server starts
# client connects
# client disconnects
# 
# client connects again