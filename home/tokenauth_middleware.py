# from django.contrib.auth.models import AnonymousUser
# from channels.db import database_sync_to_async
# from rest_framework.authtoken.models import Token
# from channels.middleware import BaseMiddleware
# import logging #new edit
# from django.conf import settings
# from Customer.models import Customers as User
# from channels.middleware import BaseMiddleware
# from jwt import decode
# from rest_framework_simplejwt.tokens import RefreshToken

# class JWTAuthMiddleware(BaseMiddleware):

#     def __init__(self, inner):
#         super().__init__(inner)
#         self.secret_key = settings.SECRET_KEY

#     def receive(self, websocket, message):
#         if message['type'] == 'websocket.connect':
#             token = message.get('headers', {}).get('Authorization', None)
#             if token:
#                 access_token = token.split()[1]
#                 try:
#                     decoded_data = decode(access_token, self.secret_key, algorithms=['HS256'])
#                     refresh_token = RefreshToken(access_token)  # Optional refresh logic
#                     user = User.objects.get(id=decoded_data['user_id'])
#                     message.scope['user'] = user
#                 except (Exception) as e:
#                     # Handle authentication error
#                     pass

#         return super().receive(websocket, message)

# from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware

@database_sync_to_async
def get_user(token_key):
    from rest_framework.authtoken.models import Token
    try:
        token = Token.objects.get(key=token_key)
        return token.user
    # except (Token.DoesNotExist, DatabaseError) as e:  # Handle both token and database errors
    #     logging.error(f"Error retrieving user for token {token_key}: {e}")
        # return AnonymousUser()
    except Token.DoesNotExist:
        from django.contrib.auth.models import AnonymousUser
        return AnonymousUser()


class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        try:
            token_key = dict(scope['headers'])[b'sec-websocket-protocol'].decode('utf-8')
        except ValueError:
            token_key = None
        scope['user'] = AnonymousUser() if token_key is None else await get_user(token_key)
        return await super().__call__(scope, receive, send)



# @database_sync_to_async
# def get_user(validated_token):
#     try:
#         user = get_user_model().objects.get(id=validated_token["user_id"])
#         # return get_user_model().objects.get(id=toke_id)
#         print(f"{user}")
#         return user
   
#     except User.DoesNotExist:
#         return AnonymousUser()



# class JwtAuthMiddleware(BaseMiddleware):
#     def __init__(self, inner):
#         self.inner = inner

#     async def __call__(self, scope, receive, send):
#        # Close old database connections to prevent usage of timed out connections
#         close_old_connections()

#         # Get the token
#         token = parse_qs(scope["query_string"].decode("utf8"))["token"][0]

#         # Try to authenticate the user
#         try:
#             # This will automatically validate the token and raise an error if token is invalid
#             UntypedToken(token)
#         except (InvalidToken, TokenError) as e:
#             # Token is invalid
#             print(e)
#             return None
#         else:
#             #  Then token is valid, decode it
#             decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
#             print(decoded_data)
#             # Will return a dictionary like -
#             # {
#             #     "token_type": "access",
#             #     "exp": 1568770772,
#             #     "jti": "5c15e80d65b04c20ad34d77b6703251b",
#             #     "user_id": 6
#             # }

#             # Get the user using ID
#             scope["user"] = await get_user(validated_token=decoded_data)
#         return await super().__call__(scope, receive, send)


# def JwtAuthMiddlewareStack(inner):
#     return JwtAuthMiddleware(AuthMiddlewareStack(inner))








# # @database_sync_to_async
# # def get_user(token_key):
# #     try:
# #         token = Token.objects.get(key=token_key)
# #         return token.user
# #     except Token.DoesNotExist:
# #         return AnonymousUser()


# # class TokenAuthMiddleware(BaseMiddleware):

# #     def __init__(self, inner):
# #         super().__init__(inner)

# #     # async def __call__(self, scope, receive, send):
# #     #     headers = dict(scope['headers'])
# #     #     if b'authorization' in headers:
# #     #         token_name, token_key = headers[b'authorization'].decode().split()
# #     #         if token_name == 'Token':
# #     #             scope['user'] = await get_user(token_key)
# #     #     return await super().__call__(scope, receive, send)
# #     async def __call__(self, scope, receive, send):
# #         try:
# #             token_key = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('token', None)
# #         except ValueError:
# #             token_key = None
# #         scope['user'] = AnonymousUser() if token_key is None else await get_user(token_key)
# #         return await super().__call__(scope, receive, send)
# @database_sync_to_async
# def get_user(token_key):
#     try:
#         token = Token.objects.get(key=token_key)
#         return token.user
#     except Token.DoesNotExist:
#         return AnonymousUser()

# class TokenAuthMiddleware(BaseMiddleware):

#     def __init__(self, inner):
#         self.inner = inner

#     async def __call__(self, scope, receive, send):
#         token_key = scope['query_string'].decode().split('=')[-1]
        
#         scope['user'] = await get_user(token_key)
        
#         return await super().__call__(scope, receive, send)
# from urllib.parse import parse_qs

# from channels.db import database_sync_to_async
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AnonymousUser
# from rest_framework_simplejwt.tokens import AccessToken, TokenError


# User = get_user_model()


# @database_sync_to_async
# def get_user(user_id):
#     try:
#         return User.objects.get(id=user_id)
#     except User.DoesNotExist:
#         return AnonymousUser()


# class WebSocketJWTAuthMiddleware:

#     def __init__(self, app):
#         self.app = app

#     async def __call__(self, scope, receive, send):
#         parsed_query_string = parse_qs(scope["query_string"])
#         token = parsed_query_string.get(b"token")[0].decode("utf-8")

#         try:
#             access_token = AccessToken(token)
#             scope["user"] = await get_user(access_token["user_id"])
#         except TokenError:
#             scope["user"] = AnonymousUser()

#         return await self.app(scope, receive, send)
    
