from django.db import models
from Property.models import Properties
from Customer.models import Customers
# Create your models here.
class Favorite(models.Model):
    idp = models.ForeignKey(Properties ,on_delete=models.CASCADE)
    idc = models.ForeignKey(Customers, on_delete=models.CASCADE)