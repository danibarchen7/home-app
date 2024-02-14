from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from .serializers import CureSerializer
# Create your views here.
class CureView(APIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = CureSerializer 