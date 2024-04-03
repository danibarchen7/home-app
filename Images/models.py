from django.db import models
from Property.models import Properties
from Customer.models import Customers
# Create your models here.

class images(models.Model):
    cid = models.ForeignKey(Customers, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Customers, height_field=None, width_field=None, max_length=None)
        
class PropertyImage(models.Model):
    pid = models.ForeignKey(Properties, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property', height_field=None, width_field=None, max_length=None)
    test = models.BooleanField(default=True)
    
    
    
    # def save(self,*args, **kwargs):
    #     input_data = self.image
    #     model = keras.models.load_model('Images/house.h5',compile=False)
    #     resize = tf.image.resize(input_data, (256,256))
    #     yhat = model.predict(np.expand_dims(resize/255, 0))
    #     if  yhat>0.5:
    #         self.save()
        
        
            
        