from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import PropertiesSerializer
from .models import Properties
# Create your views here.

class PropertiesView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class =  PropertiesSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get (self,request):
        property = Properties.objects.all()
        serializer = PropertiesSerializer(property, many=True)
        return Response(serializer.data)
    
    
class SingleProperty(APIView):
    serializer_class = PropertiesSerializer
    
    def get(self,request,pk):
        property = Properties.objects.get(id = pk)
        seriralizer = PropertiesSerializer(property)
        return Response(seriralizer.data)
    
    def delete(self,request,pk):
      property = Properties.objects.get(id=pk)
      property.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):

        property = Properties.objects.get(id=pk)
        serializer = PropertiesSerializer(property, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)