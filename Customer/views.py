from django.shortcuts import render
from rest_framework import permissions,generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate , login
from rest_framework.authtoken.models  import Token
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer, RegisterSerializer
from .models import Customers
# Create your views here.




from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            request.META['HTTP_AUTHORIZATION'] = 'Token ' + token.key
            user_serilizer = CustomUserSerializer(user)
            return Response({"token": token.key,
                             "user":user_serilizer.data,
                            })
        else:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        session = request.session
        session.flush()
        return Response({'message': 'Logout successful'})



class CustomUserViewSet(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)
    def get(self,request):
        user = Customers.objects.all()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
    

class SingleCustomerView(APIView):
    serializer_class = CustomUserSerializer
    def get(self,request,pk):
        customer = Customers.objects.get(id=pk)
        serializer = self.serializer_class(customer)
        return Response(serializer.data)


from django.shortcuts import render
from .serializers import UserSerializer
from .models import Customers as User
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def user_list(request, ):
    users = User.objects.all().order_by('username')
    serializer = UserSerializer(instance=users, many=True)
    return Response(serializer.data)
