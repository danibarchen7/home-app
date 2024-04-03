from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from .serializers import CommentSerializers

# Create your views here.

class CommentsView(APIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = CommentSerializers
    def get (self,request):
        comment = Comments.objects.all()
        serializer = CommentSerializers(comment, many=True)
        return Response(serializer.data)
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import Comments
class PredictView(APIView):
    permission_classes= (AllowAny,)
    serializer_class = CommentSerializers
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleComment(APIView):
    def get (self,request,pk):
        comment = Comments.objects.get(id=pk)
        serializer = CommentSerializers(comment, many=False)
        return Response(serializer.data)
    def delete(self,request,pk):
      comment = CommentSerializers.objects.get(id=pk)
      comment.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):

        comment = Comments.objects.get(id=pk)
        serializer = CommentSerializers(comment, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)