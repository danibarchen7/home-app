from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from .serializers import CommentSerializers

# Create your views here.

class CommentsView(APIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = CommentSerializers
    

from rest_framework.views import APIView
from rest_framework.response import Response
import tensorflow as tf
from tensorflow import keras
import os
from tensorflow.keras.layers import TextVectorization
import numpy as np
import pandas as pd
from rest_framework.permissions import AllowAny

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'false'
class PredictView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        data = request.data
        input_data = data['input_data']
        df = pd.read_csv(os.path.join('Comments','train.csv','train.csv'))
        X = df['comment_text']
        vectorizer = TextVectorization(max_tokens=200000,
                               output_sequence_length=1800,
                               output_mode='int')
        vectorizer.adapt(X.values)
        input_data = vectorizer(input_data)
        # input_data = tf.strings.unicode_decode(input_data, 'UTF-8')
        model = keras.models.load_model('Comments/toxicity.h5')
        prediction = model.predict(np.expand_dims(input_data,0))
        good =True
        for idx, col in enumerate(df.columns[2:]):
            if prediction[0][idx]>0.1:
                good = False
            else:
                good = True    
        return Response({'prediction': good})


