from django.shortcuts import render
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CureSerializer
# Create your views here.
class CureView(APIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = CureSerializer 
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            return Response(serializer.data,status = status.HTTP_201_CREATED)