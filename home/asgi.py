"""
ASGI config for home project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

# application = get_asgi_application()





import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from chat.consumers import ChatConsumer
from django.urls import include, path, re_path
from .tokenauth_middleware import TokenAuthMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            TokenAuthMiddleware(
                URLRouter(
                    [
                        re_path(r'', ChatConsumer.as_asgi())
                    ]
                )
            ),
        ),
    }
)












# import os

# from channels.routing import ProtocolTypeRouter
# from django.core.asgi import get_asgi_application
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
# from django.core.asgi import get_asgi_application

# from chat.routing import websocket_urlpatterns
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home.settings")

# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         # Just HTTP for now. (We can add other protocols later.)
#         "websocket": AllowedHostsOriginValidator(
#             AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
#         ),
#     }
# )

# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.urls import re_path
# from .consumers import ChatConsumer
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             [
#                 # Your routing configuration here
#                 re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
#             ]
#         )
#     ),
# })
# import os
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# from django.urls import path,include

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
    # "websocket": AuthMiddlewareStack(
    #     URLRouter(
    #          path("", include("home.urls"))
    #     )
#     ),
# })
# import os

# from channels.routing import ProtocolTypeRouter
# from channels.auth import AuthMiddlewareStack
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path , include

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')
# # Initialize Django ASGI application early to ensure the AppRegistry
# # is populated before importing code that may import ORM models.
# django_asgi_app = get_asgi_application()

# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#     # Just HTTP for now. (We can add other protocols later.)
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#              path("", include("chat.urls"))
#         )),
# })

# import os
# from django.urls import path
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from channels.security.websocket import AllowedHostsOriginValidator
# from chat.consumers import ChatConsumer
# from chat.urls import urlpatterns

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

# application = ProtocolTypeRouter({
#     'http':get_asgi_application(),
#         "websocket": AllowedHostsOriginValidator(
#             AuthMiddlewareStack(URLRouter(urlpatterns))
#         ),
# })

# import os

# from channels.routing import URLRouter, ProtocolTypeRouter
# from channels.security.websocket import AllowedHostsOriginValidator  # new
# from django.core.asgi import get_asgi_application
# from chat import routing  # new
# from .tokenauth_middleware import TokenAuthMiddleware  # new
# from channels.auth import AuthMiddlewareStack

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AllowedHostsOriginValidator(  # new
#         TokenAuthMiddleware(URLRouter(routing.websocket_urlpatterns)))
# })
