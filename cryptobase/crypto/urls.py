from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('prices/', views.prices, name="prices"),
    path('weather/', views.weather, name="weather"),
    path('wiki/', views.wiki, name="wiki"),
    path('covid/', views.covid, name="covid"),
]
