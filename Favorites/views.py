from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions,status
from rest_framework.views import APIView
from .serializers import FavoriteSerializer
from .models import Favorite

# Create your views here.
class FavoriteView(APIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = FavoriteSerializer 
    def get(self,request):
        fav = Favorite.objects.all()
        serializer = self.serializer_class(fav, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
    
    
        

class SingleFavoriteView(APIView):
    serializer_class = FavoriteSerializer
    def get(self,request,pk):
        fav = Favorite.objects.get(idc=pk)
        serializer = FavoriteSerializer(fav)
        return Response(serializer.data)
    
    def delete(self,request,pk):
      fav = Favorite.objects.get(idc=pk)
      fav.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self,request,pk):
        fav = Favorite.objects.get(idc=pk)
        serializer = FavoriteSerializer(fav, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        