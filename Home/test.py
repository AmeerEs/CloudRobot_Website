import socket
import re


print("\nWelcome to Chat Room\n")
print("Initialising....\n")

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = "Web_Server"
        
s.listen(5)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
conn.send(name.encode())

while True:
    print("yes ?")
    message = conn.recv(1024)
    message = message.decode()
    if message == "Left chat room!":
        print(s_name, message)
        break
    elif message.find("t") != -1:
        sensorN = "Temprature"
    elif message.find("h") != -1:
        sensorN = "Humidity"
    else:
        print(message)

    print(s_name, ":", message)
    valueN = re.findall("\d+.\d+", message)
    print(sensorN, "=", valueN)