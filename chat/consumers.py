

import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

# # from channels.generic.websocket import AsyncWebsocketConsumer
# # import json

# # class ChatConsumer(AsyncWebsocketConsumer):
# #     async def connect(self):
# #         await self.accept()

# #     async def disconnect(self, close_code):
# #         pass

# #     async def receive(self, text_data):
# #         text_data_json = json.loads(text_data)
# #         message = text_data_json['message']

# #         await self.send(text_data=json.dumps({
# #             'message': message
# #         }))
# # consumers.py
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# import pusher  # Assuming you've installed the pusher library

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         # Join the chat room group
#         await self.channel_layer.group_add(
#             'chat_room',
#             self.channel_name
#         )
#         await self.accept()

    
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         # Broadcast message to the group
#         await self.channel_layer.group_send(
#             'chat_room',
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#         await self.close()
#     async def chat_message(self, event):
#         message = event['message']

#         # Optionally, send message using Pusher (if you want to use Pusher)
#         pusher_client = pusher.Pusher(
#             app_id='1735915',
#             key='a8a6dcdd8e2cadbf2718',
#             secret='adcb09443d95cde06f8e',
#             cluster='ap2'
#         )
#         pusher_client.trigger('chat_channel', 'new_message', {'message': message})

#         # Send message back to the WebSocket client
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))
#     async def disconnect(self, close_code):
#         # Discard from the chat room group
#         await self.channel_layer.group_discard(
#             'chat_room',
#             self.channel_name
#         )
# import json

# from channels.generic.websocket import AsyncWebsocketConsumer


# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope["ws/chat"]["kwargs"]["room_name"]
#         self.room_group_name = f"chat_{self.room_name}"

#         # Join room group
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)

#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]

#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name, {"type": "chat.message", "message": message}
#         )

#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event["message"]

#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({"message": message}))
# from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import sync_to_async
# from .models import Chatroom,ChatMessage
# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         chatroom_name = self.scope['url_route']['kwargs']['chatroom_name']
#         chatroom = await sync_to_async(Chatroom.objects.get)(name=chatroom_name)

#         self.chatroom = chatroom
#         self.room_group_name = f"chatroom_{chatroom.id}"

#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )

#         await self.accept()

#     async def receive(self, text_data):
#         message = text_data.decode()

#         chat_message = ChatMessage(
#             chatroom=self.chatroom,
#             sender=self.scope['user'],
#             message=message
#         )
#         chat_message.save()

#         await self.broadcast_message(message)

#     async def broadcast_message(self, message):
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )

#     async def disconnect(self, close_code):
#         # Discard from the chat room group
#         await self.channel_layer.group_discard(
#             'chat_room',
#             self.channel_name
#         )

# import base64
# import json
# import secrets
# from datetime import datetime

# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
# from django.core.files.base import ContentFile

# from Customer.models import Customers
# from .models import Message, Conversation
# from .serializers import MessageSerializer
# from channels.generic.websocket import AsyncWebsocketConsumer

# class ChatConsumer(AsyncWebsocketConsumer):
#     def connect(self):
#         print("here")
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = f"chat_{self.room_name}"

#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name, self.channel_name
#         )
#         self.accept()

#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )

#     # Receive message from WebSocket
#     def receive(self, text_data=None, bytes_data=None):
#         # parse the json data into dictionary object
#         text_data_json = json.loads(text_data)

#         # Send message to room group
#         chat_type = {"type": "chat_message"}
#         return_dict = {**chat_type, **text_data_json}
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             return_dict,
#         )

#     # Receive message from room group
#     def chat_message(self, event):
#         text_data_json = event.copy()
#         text_data_json.pop("type")
#         message, attachment = (
#             text_data_json["message"],
#             text_data_json.get("attachment"),
#         )

#         conversation = Conversation.objects.get(id=int(self.room_name))
#         sender = self.scope['user']

#         # Attachment
#         if attachment:
#             file_str, file_ext = attachment["data"], attachment["format"]

#             file_data = ContentFile(
#                 base64.b64decode(file_str), name=f"{secrets.token_hex(8)}.{file_ext}"
#             )
#             _message = Message.objects.create(
#                 sender=sender,
#                 attachment=file_data,
#                 text=message,
#                 conversation_id=conversation,
#             )
#         else:
#             _message = Message.objects.create(
#                 sender=sender,
#                 text=message,
#                 conversation_id=conversation,
#             )
#         serializer = MessageSerializer(instance=_message)
#         # Send message to WebSocket
#         self.send(
#             text_data=json.dumps(
#                 serializer.data
#             )
#         )

# from channels.generic.websocket import AsyncWebsocketConsumer
# import json

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#         await self.accept()
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type':'tester_message',
#                 'tester':'tester',
#             }
#         )
        
#     async def tester_message(self,event):
#         tester = event['tester']
#         await self.send(text_data=json.dumps({
#             'tester':tester,
#         }))
    
#     async def disconnect(self, code):
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )    