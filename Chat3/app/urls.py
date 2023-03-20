from django.urls import path
from .views import Home
urlpatterns = [
    path('<str:groupkaname>',Home,name="home"),
]
