from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
import tensorflow as tf
from tensorflow import keras
import os
class PredictView(APIView):
    def post(self, request):
        data = request.data
        model = keras.models.load_model('Images/house.h5')
        resize = tf.image.resize(data, (256,256))
        yhat = model.predict(np.expand_dims(resize/255, 0))
        return Response({'prediction': yhat})