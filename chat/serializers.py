from Customer.serializers import UserSerializer
from .models import Conversation, Message,Notification
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Message
    #     exclude = ('conversation_id',)
    sender = UserSerializer()

    class Meta:
        model = Message
        fields = ['id', 'sender', 'text', 'attachment', 'timestamp']


class ConversationListSerializer(serializers.ModelSerializer):
    initiator = UserSerializer()
    receiver = UserSerializer()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['id','initiator', 'receiver', 'last_message']

    # def get_last_message(self, instance):
    #     message = instance.message_set.first()
    #     return MessageSerializer(instance=message)
    def get_last_message(self, instance):
        try:
            message = instance.message_set.latest('timestamp')
            return MessageSerializer(instance=message).data
        except Message.DoesNotExist:
            return None


class ConversationSerializer(serializers.ModelSerializer):
    initiator = UserSerializer()
    receiver = UserSerializer()
    message_set = MessageSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['id','initiator', 'receiver', 'message_set']

class NotificationSerializer(serializers.ModelSerializer):
    model =Notification
    fields = '__all__'