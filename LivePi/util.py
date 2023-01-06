import socket
import time
import threading
from Home.models import *
import datetime



class CreateClientThread(threading.Thread):

    def __init__(self, s):
            threading.Thread.__init__(self)
            self.s = s

    def run(self):
        try:
            print("\nWelcome to Chat Room\n")
            print("Initialising....\n")
            time.sleep(1)

            host = "192.168.43.36"
            ip = socket.gethostbyname(host)
            port = 1235
            print(host, "(", ip, ")\n")
            name = "Robot1"
            print("\nTrying to connect to ", host, "(", port, ")\n")
            time.sleep(1)
            self.s.connect((host, port))
            print("Connected...\n")

            self.s.send(name.encode())
            s_name = self.s.recv(1024)
            s_name = s_name.decode()
            print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

        except Exception as e:
            print(e)


def sendCommand(text, s):
    try:    
            message = text
            c = 0
            if message == "f":
                c = 3
            elif message == "l":
                c = 5
            elif message == "r":
                c = 6
            elif message == "b":
                c = 4
            elif message == "s":
                c = 7
            else:
                print("no")
            print(message)
            s.send(message.encode())

    except Exception as e:
        print(e)