from django.db.models.query import QuerySet
from django.shortcuts import render
from .serializers import TipeSerializer
from rest_framework import permissions ,status,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tipe
# Create your views here.

class TipeListView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Tipe.objects.all()
    serializer_class = TipeSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SingleTipeView(APIView):
    def get (self,request,pk):
        tipes = Tipe.objects.get(id=pk)
        serializer = TipeSerializer(tipes)
        return Response(serializer.data)
    def delete(self,request,pk):
      tipe = Tipe.objects.get(id=pk)
      tipe.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):

        tipe = Tipe.objects.get(doctor=pk)
        serializer = TipeSerializer(tipe, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

