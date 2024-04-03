       
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
import tensorflow as tf
# from tensorflow import keras
import numpy as np
from .serializers import ImagesSerializer, PropertyImageSerializer
from .models import images, PropertyImage
from Property.models import Properties





from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FileUploadParser  

from .models import PropertyImage
from .serializers import PropertyImageSerializer
from keras.models import load_model


from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.serializers import ModelSerializer  # Assuming PropertyImageSerializer inherits from ModelSerializer

import tensorflow as tf
from tensorflow.keras.models import load_model  # Assuming load_model is a custom function or utility

class PredictView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PropertyImageSerializer
    parser_classes = (MultiPartParser, FileUploadParser)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            image = request.FILES['image']

            # Read image data from the uploaded file
            image_data = image.read()

            # Preprocess image (decode and resize)
            image_tensor = tf.image.decode_jpeg(image_data, channels=3)  # Assuming image is JPEG
            image_tensor = tf.image.resize(image_tensor, (256, 256))
            image_tensor = image_tensor / 255.0  # Normalize pixel values

            # Load the pre-trained model
            model = load_model("Images/house3.h5")

            # Make prediction
            yhat = model.predict(np.expand_dims(image_tensor, axis=0))

            if yhat < 0.5:  # Assuming this is your classification threshold
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Image classification failed.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
class SinglePropertyImg(APIView):
    serializer_class = PropertyImageSerializer
    def get(self,request,pk):
        pimg = PropertyImage.objects.get(pid=pk)
        serializer = PropertyImageSerializer(pimg,many=True)
        return Response(serializer.data)
    
    def delete(self,request,pk):
      imag = images.objects.get(pid=pk)
      imag.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
  
    def put(self,request,pk):
        pimg = PropertyImage.objects.get(pid=pk)
        serializer = PropertyImageSerializer(pimg, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)       
        
class ProfileImage(APIView):
    serializer_class = ImagesSerializer
    def get(self,request):
        img = images.objects.all()
        serializer = ImagesSerializer(img, many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)     
        
class SingleImageProfile(APIView):
    serializer_class = ImagesSerializer
    def get(self,request,pk):
        img = images.objects.get(cid = pk)
        seriralizer = ImagesSerializer(img)
        return Response(seriralizer.data)
    
    def delete(self,request,pk):
      imag = images.objects.get(cid=pk)
      imag.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        img = images.objects.get(cid=pk)
        serializer = ImagesSerializer(img, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
