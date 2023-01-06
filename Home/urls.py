from django.urls import path

from . import views

app_name = "Home"
urlpatterns = [
    path("CloudRobot/", views.index, name="index"),
    path("verify/", views.login_view, name="login"),
    path("measurements/", views.show_measurements, name="measurement"),
    path("logout/", views.logout_view, name="logout"),
    path("totalM/", views.totalM, name="totalM"),
    path("totalT/", views.totalT, name="totalT"),
    path("totalE/", views.totalE, name="totalE"),
    path("totalW/", views.totalW, name="totalW"),
]