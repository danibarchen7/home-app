# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter,URLRouter
# import chat.routing
# # application = ProtocolTypeRouter({
# #         'websocket':AuthMiddlewareStack(
# #           URLRouter(
# #               chat.routing.websocket_urlpatterns
# #           )  
# #         ),
           
# # })
# # from channels.routing import ProtocolTypeRouter, URLRouter
# # from django.urls import path
# # from chat import consumers
# # from django.core.asgi import get_asgi_application

# # application = ProtocolTypeRouter({
# #     "http": get_asgi_application(),
# #     "websocket": URLRouter([
# #         path("ws/chat/<str:room_name>/", consumers.ChatConsumer.as_asgi()),
# #     ]),
# # })

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from chat.consumers import ChatConsumer
from .tokenauth_middleware import TokenAuthMiddleWare

application = ProtocolTypeRouter(
	{
		"websocket": TokenAuthMiddleWare(
			AllowedHostsOriginValidator(
				URLRouter(
				[path("", ChatConsumer.as_asgi())]
				)
			)
		)
	}
)
