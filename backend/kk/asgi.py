import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kk.settings")

django_asgi_app = get_asgi_application()

from scripts.middleware import JwtAuthMiddleware
import scripts.urls

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": JwtAuthMiddleware(
        URLRouter(scripts.urls.websocket_urlpatterns)
    ),
})
