from django.urls import path
from .consumer import MySyncConsumer,MyASyncConsumer


websocket_urlpatterns = [
    path('ws/sc/<str:groupname>/',MySyncConsumer.as_asgi()),
    path('ws/asc/',MyASyncConsumer.as_asgi()),
]