from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .models import Conversation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Customer.models import Customers as User
from .serializers import ConversationListSerializer, ConversationSerializer
from django.db.models import Q


from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer

@api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
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
from .serializers import ConversationSerializer,NotificationSerializer

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


 


from rest_framework import authentication, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

class MessageSendAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "You are not authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "general", {"type": "send_info_to_user_group",
                        "text": {"status": "done"}}
        )

        return Response({"status": True}, status=status.HTTP_200_OK)



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



class NotificationView(APIView):
    serializer_class = NotificationSerializer
    permission_classes = (AllowAny,)
    def get(self,request):
        pass

class ConView(APIView):
    def get (self,request,pk):
        pass