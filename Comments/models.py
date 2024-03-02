from django.db import models
from Customer.models import Customers
from Property.models import Properties
# Create your models here.
import tensorflow as tf
from tensorflow import keras
import os
from tensorflow.keras.layers import TextVectorization
import numpy as np
import pandas as pd



class Comments(models.Model):
    idc = models.ForeignKey(Customers,on_delete=models.CASCADE)
    idp = models.ForeignKey(Properties,on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    comments = models.CharField(max_length=2000)
    evaluation = models.BooleanField()
    def create_related(self):
        input_data = self.comments
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
        for idx, col in enumerate(df.columns[2:]):
            if prediction[0][idx]>0.1:
                evaluation = False
            else:
                evaluation = True 
    
    def update_counter(self):
        pro = Properties.objects.get(id=self.idp)
        if self.evaluation:
            pro.counter +=1
        
        