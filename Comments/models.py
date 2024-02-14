from django.db import models
from Customer.models import Customers
from Property.models import Properties
# Create your models here.
class Comments(models.Model):
    idc = models.ForeignKey(Customers,on_delete=models.CASCADE)
    idp = models.ForeignKey(Properties,on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    comments = models.CharField(max_length=2000)
    evaluation = models.BooleanField()
    