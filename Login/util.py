from Home.models import *
import socket
import threading
import datetime
import re
from django.contrib import messages
import winsound
import ctypes
MB_OK = 0x0
MB_OKCXL = 0x01
MB_YESNOCXL = 0x03
MB_YESNO = 0x04
MB_HELP = 0x4000
ICON_EXLAIM=0x30
ICON_INFO = 0x40
ICON_STOP = 0x10



class CreateServerThread(threading.Thread):

    def __init__(self):
            threading.Thread.__init__(self)

    def run(self):
        try:
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
            print(s_name, "has connected...\nEnter [e] to exit chat room\n")
            conn.send(name.encode())

            while True:
                r = False
                d = False
                message = conn.recv(1024)
                message = message.decode()
                if message == "Left chat room!":
                    print(s_name, message)
                    break
                elif message.find("t") != -1:
                    r = True
                    sensorN = 1
                elif message.find("h") != -1:
                    r = True
                    sensorN = 2
                elif message.find("g") != -1:
                    r = True
                    sensorN = 5
                elif message.find("w") != -1:
                    d = True
                else:
                    print(message)
            
                if r:
                    print(s_name, ":", message)
                    valueN = re.findall(r"-?\d+.\d+|-?\d+", message)
                    measurement(sensor=sensor.objects.get(pk=sensorN), value=(valueN[1]), time=datetime.datetime.now(), agent=agent.objects.get(pk=valueN[0])).save()
                    if float(valueN[1]) >= threshold.objects.get(pk=sensorN).max_value:
                        s = "Max."
                        warning(sensor=sensor.objects.get(pk=sensorN) ,agent=agent.objects.get(pk=valueN[0]), value=valueN[1], status=s, time=datetime.datetime.now()).save()
                        winsound.PlaySound("E:/Aimed_Development/College Project/CloudRobot/Home/static/Home/sound/bleep.wav", winsound.SND_ASYNC)

                    elif float(valueN[1]) <= threshold.objects.get(pk=sensorN).min_value:
                        s= "Min."
                        warning(sensor=sensor.objects.get(pk=sensorN) ,agent=agent.objects.get(pk=valueN[0]), value=valueN[1], status=s, time=datetime.datetime.now()).save()
                        winsound.PlaySound("E:/Aimed_Development/College Project/CloudRobot/Home/static/Home/sound/bleep.wav", winsound.SND_ASYNC)
                if d:
                    print(s_name, ":", message)
                    winsound.PlaySound("E:/Aimed_Development/College Project/CloudRobot/Home/static/Home/sound/bleep.wav", winsound.SND_ASYNC)
                    result = ctypes.windll.user32.MessageBoxW(0, "Warning Message!", "Person detected!", MB_OK | ICON_EXLAIM)

                
        except Exception as e:
            print(e)
            
            
