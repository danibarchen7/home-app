# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from chat.views import ChatroomViewSet, ChatMessageViewSet
# from chat.consumers import ChatConsumer

# router = DefaultRouter()
# router.register(r'chatrooms', ChatroomViewSet)
# router.register(r'chatmessages', ChatMessageViewSet)

# urlpatterns = [
    
#     path('ws/chatrooms/<chatroom_name>/', ChatConsumer.as_asgi()),
# ]

from django.urls import path
from . import views
from . import consumers

urlpatterns = [
    path('start/', views.start_convo),
    path('start/<int:conv_id>', views.post_message),
    path('<int:convo_id>/', views.get_conversation, name='get_conversation'),
    path('', views.conversations, name='conversations'),
    path('new/', views.your_view, name='new'),
    
]
