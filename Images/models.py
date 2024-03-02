from django.db import models
from Property.models import Properties
from Customer.models import Customers
# Create your models here.
class images(models.Model):
    cid = models.ForeignKey(Customers, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Customers, height_field=None, width_field=None, max_length=None)
        
class PropertyImage(models.Model):
    pid = models.ForeignKey(Properties, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=property, height_field=None, width_field=None, max_length=None)