from django.urls import path

from . import views

app_name = "LivePi"
urlpatterns = [
    path("", views.index, name="index"),

]