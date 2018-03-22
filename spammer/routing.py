"""Routing files that redirects clients to consumers.

See Channels documentation for detail.
"""

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumers import ClientSocketConsumer


application = ProtocolTypeRouter({
    # WebSocket chat handler
    "websocket": URLRouter([
        path('ws/', ClientSocketConsumer),
    ]),
})
