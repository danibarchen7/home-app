from Customer.models import Customers
from django.db import models
from Property.models import Properties
# Create your models here.
class Cures(models.Model):
    HOUSE = "HO"
    SHOP = "SH"
    FARME = "FA"
    HOLE = "HL"
    realstates = [
        (HOUSE,"Houses"),
        (HOLE,"Hole"),
        (SHOP,"Shop"),
        (FARME,"Farme")
    ]
    idp = models.ForeignKey(Properties, on_delete=models.CASCADE)
    idc = models.ForeignKey(Customers, on_delete=models.CASCADE)
    Type = models.CharField( max_length=2,
                    choices=realstates,
                    default="HO"
    )
