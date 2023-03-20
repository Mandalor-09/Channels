"""
ASGI config for Chat3 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from app.routing import websocket_urlpatterns
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Chat3.settings")

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket":URLRouter(websocket_urlpatterns)
})
