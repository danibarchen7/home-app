from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import PropertiesSerializer
# Create your views here.

class PropertiesView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class =  PropertiesSerializer