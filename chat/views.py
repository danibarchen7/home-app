# from django.conf import settings
# from django.http import HttpResponse
# from django.shortcuts import render

# # Create your views here.
# # views.py
# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from pusher import Pusher

# # PUSHER_APP_ID = '1735915'
# # PUSHER_KEY = 'a8a6dcdd8e2cadbf2718'
# # PUSHER_SECRET = 'adcb09443d95cde06f8e'
# # PUSHER_CLUSTER = 'ap2'

# # pusher = Pusher(
# #     app_id=PUSHER_APP_ID,
# #     key=PUSHER_KEY,
# #     secret=PUSHER_SECRET,
# #     cluster=PUSHER_CLUSTER,
# #     ssl=True
# # )

# # class SendMessage(APIView):
# #     def post(self, request):
# #         message = request.data['message']
# #         pusher.trigger('chat', 'message', {'message': message})
# #         return Response({'status': 'success'})
# # from django.db.models import QuerySet
# # from rest_framework import viewsets
# # from .models import Chatroom

# # class ChatroomViewSet(viewsets.ModelViewSet):
# #     queryset = Chatroom.objects.all()


# # from django.contrib.auth.models import User
# from .models import ChatMessage
# from django.db.models import Q
# from rest_framework import filters
# from rest_framework import viewsets
# from Customer.models import Customers

# class ChatMessageViewSet(viewsets.ModelViewSet):
#     queryset = ChatMessage.objects.all()
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('chatroom__name', 'sender__username', 'message')
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .models import Conversation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Customer.models import Customers as User
from .serializers import ConversationListSerializer, ConversationSerializer
from django.db.models import Q
from django.shortcuts import redirect, reverse


# Create your views here.
# @api_view(['POST'])
# def start_convo(request, ):
#     data = request.data
#     username = data.get('username')
#     try:
#         participant = User.objects.get(username=username)
#     except User.DoesNotExist:
#         return Response({'message': 'You cannot chat with a non existent user'})

#     conversation = Conversation.objects.filter(Q(initiator=request.user, receiver=participant) |
#                                                Q(initiator=participant, receiver=request.user))
#     if conversation.exists():
#         return redirect(reverse('get_conversation', args=(conversation[0].id,)))
#     else:
#         conversation = Conversation.objects.create(initiator=request.user, receiver=participant)
#         return Response(ConversationSerializer(instance=conversation).data)

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_message(request, conv_id):
    data = request.data
    try:
        conversation = Conversation.objects.get(id=conv_id)
    except Conversation.DoesNotExist:
        return Response({'message': 'Conversation not found'})

    if request.user not in [conversation.initiator, conversation.receiver]:
        return Response({'message': 'You are not authorized to post a message in this conversation'})

    message = Message.objects.create(
        sender=request.user,
        conversation_id=conversation,
        text=data.get('text', ''),
        attachment=data.get('attachment', ''),
    )

    serializer = MessageSerializer(instance=message)
    return Response(serializer.data)

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import get_object_or_404
from .models import Conversation
from .serializers import ConversationSerializer

@api_view(['POST'])
def start_convo(request):
    data = request.data
    username = data.get('username')
    try:
        participant = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'message': 'You cannot chat with a non existent user'})

    conversation = Conversation.objects.filter(Q(initiator=request.user, receiver=participant) |
                                               Q(initiator=participant, receiver=request.user))
    if conversation.exists():
        conversation = conversation[0]
        url = reverse('get_conversation', args=(conversation.id,), request=request)
        return Response({'message': 'Conversation already exists', 'url': url})
    else:
        conversation = Conversation.objects.create(initiator=request.user, receiver=participant)
        url = reverse('get_conversation', args=(conversation.id,), request=request)
        return Response({'message': 'Conversation created', 'url': url})



@api_view(['GET'])
def get_conversation(request, convo_id):
    conversation = Conversation.objects.filter(id=convo_id)
    if not conversation.exists():
        return Response({'message': 'Conversation does not exist'})
    else:
        serializer = ConversationSerializer(instance=conversation[0])
        return Response(serializer.data)


@api_view(['GET'])
def conversations(request):
    conversation_list = Conversation.objects.filter(Q(initiator=request.user) |
                                                    Q(receiver=request.user))
    serializer = ConversationListSerializer(instance=conversation_list, many=True)
    return Response(serializer.data)


from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .models import Message


# class MessageSendAPIView(APIView):
#     
#     authentication_classes = [authentication.JSONWebTokenAuthentication]
#     def get(self, request):
#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_send)(
#             "general", {"type": "send_info_to_user_group",
#                         "text": {"status": "done"}}
#         )

#         return Response({"status": True}, status=status.HTTP_200_OK)
        
#     def post(self, request):
        
#            msg = Message.objects.create(sender=request.user, text={
#                                      "message": request.data["text"]})
#            socket_message = f"Message with id {msg.id} was created!"
#            channel_layer = get_channel_layer()
#            async_to_sync(channel_layer.group_send)(
#              f"{request.user.id}-message", {"type": "send_last_message",
#                                            "text": socket_message}
#               )

#            return Response({"status": True}, status=status.HTTP_201_CREATED)
        


from rest_framework import authentication, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

class MessageSendAPIView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "You are not authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "general", {"type": "send_info_to_user_group",
                        "text": {"status": "done"}}
        )

        return Response({"status": True}, status=status.HTTP_200_OK)


    # def post(self, request):
    #  if not request.user.is_authenticated:
    #     return Response({"error": "You are not authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)

    #  recipient = User.objects.get(id=request.data.get("username"))
    #  conversation = Conversation.objects.filter(Q(participant1=request.user, participant2=recipient) |
    #                                           Q(participant1=recipient, participant2=request.user)).first()
    #  if not conversation:
    #     conversation = Conversation.objects.create(participant1=request.user, participant2=recipient)

    #  msg = Message.objects.create(sender=request.user, text={"message": request.data["text"]}, conversation_id=conversation)
    #  socket_message = f"Message with id {msg.id} was created!"
    #  channel_layer = get_channel_layer()
    #  async_to_sync(channel_layer.group_send)(
    #     f"{request.user.id}-message", {"type": "send_last_message",
    #                                    "text": socket_message}
    # )

    #  return Response({"status": True}, status=status.HTTP_201_CREATED)
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "You are not authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)

        msg = Message.objects.create(sender=request.user, text={
                                     "message": request.data["text"]})
        socket_message = f"Message with id {msg.id} was created!"
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"{request.user.id}-message", {"type": "send_last_message",
                                           "text": socket_message}
        )

        return Response({"status": True}, status=status.HTTP_201_CREATED)



from pusher import Pusher
@api_view(['GET'])
def your_view(request):
    pusher = Pusher(
        app_id=settings.PUSHER_APP_ID,
        key=settings.PUSHER_KEY,
        secret=settings.PUSHER_SECRET,
        cluster=settings.PUSHER_CLUSTER,
        ssl=True
    )

    pusher.trigger('username', 'your_event', {'message': 'Hello, world!'})

    return HttpResponse('Message sent!')

# from django.contrib.auth.decorators import login_required
# from rest_framework import generics, status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Conversation, Message
# from .serializers import ConversationListSerializer, ConversationSerializer, MessageSerializer
# from django.conf import settings
# from Customer.models import Customers


# class CreateMessage(APIView):
#     permission_classes = (IsAuthenticated,)

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         sender = self.request.user
#         conversation_id = data.get('conversation_id')
#         try:
#             conversation = Conversation.objects.get(id=conversation_id)
#         except Conversation.DoesNotExist:
#             return Response({"error": "Conversation not found"}, status=status.HTTP_404_NOT_FOUND)

#         if not (conversation.initiator == sender or conversation.receiver == sender):
#             return Response({"error": "Unauthorized access"}, status=status.HTTP_401_UNAUTHORIZED)

#         text = data.get('text', '')
#         attachment = request.FILES.get('attachment')
#         message = Message.objects.create(sender=sender, text=text, attachment=attachment, conversation_id=conversation)
#         return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)


# class GetConversations(generics.ListAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ConversationListSerializer

#     def get_queryset(self):
#         user = self.request.user
#         queryset = Conversation.objects.filter(initiator=user) | Conversation.objects.filter(receiver=user)
#         return queryset


# class GetConversationDetail(generics.RetrieveAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ConversationSerializer
#     lookup_field = 'id'

#     def get_queryset(self):
#         user = self.request.user
#         queryset = Conversation.objects.filter(initiator=user) | Conversation.objects.filter(receiver=user)
#         return queryset