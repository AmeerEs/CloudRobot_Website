from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from . import util
from .models import *
from django.urls import reverse


# Create your views here.

def index(request):
    return render(request, "Home/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password =request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('Home:index'))
        else:
            return render(request, "Login/index.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "Home/index.html")


def show_measurements(request):
    return render(request, "home/measurements.html", {
        "measurements":measurement.objects.all().order_by('-time')[:10]
    })

def totalM(request):
    return render(request, "home/totalM.html", {
        "totalM":measurement.objects.count()
    })

def totalT(request):
    return render(request, "home/totalT.html", {
        "totalT":task.objects.count()
    })

def totalE(request):
    return render(request, "home/totalE.html", {
        "totalE":event.objects.count()
    })

def totalW(request):
    return render(request, "home/totalW.html", {
        "totalW":warning.objects.count()
    })



def logout_view(request):
    return None