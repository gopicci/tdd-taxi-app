from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter

from taxi.middleware import TokenAuthMiddlewareStack
from trips.consumers import TaxiConsumer


# http uses implicit settings, websocket needs to be explicit
application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddlewareStack(
        URLRouter([
            path('taxi/', TaxiConsumer),
        ])
    ),
})
