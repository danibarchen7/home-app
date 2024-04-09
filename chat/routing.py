# import os

# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# import chat.routing

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')

# application = ProtocolTypeRouter({
#     'http':get_asgi_application(),
#     'websocket':AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     )
# })
# from django.urls import re_path

# from . import consumers

# websocket_urlpatterns = [
#     re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
# ]
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path

# from chat.consumers import ChatConsumer

# application = ProtocolTypeRouter({
#     'websocket': URLRouter([
#         path('ws/chatrooms/<chatroom_name>/', ChatConsumer.as_asgi()),
#     ]),
# })

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r"ws/notify/", consumers.ChatConsumer.as_asgi()),
]
