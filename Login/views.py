from django.http import HttpResponse
from . import util
from django.shortcuts import render

# Create your views here.
def index(request):
    util.CreateServerThread().start()
    return render(request, "Login/index.html")
    