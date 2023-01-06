from django.shortcuts import render
from . import util
import socket
import time
 
# Create your views here.

s= socket.socket()

def index(request):
    
    util.CreateClientThread(s).start()
    text = request.GET.get('button_command')
    util.sendCommand(text, s)
    
    return render(request, "LivePi/index.html")


