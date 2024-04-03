from django.db import models
from Customer.models import Customers

# Create your models here.
class Properties(models.Model):
    HOME = "HO"
    SHOP = "SH"
    LOUNG = "LO"
    ROOM = "RO"
    CHALEH = "CH"
    VILLA = "VI"
    FARM = "FA"
    PROPERTY_CHOICES =[
        (HOME,"Home"),
        (SHOP,"Shop"),
        (LOUNG,"Loung"),
        (ROOM,"Room"),
        (CHALEH,"Chaleh"),
        (VILLA,"Villa"),
    ]
    
    idt = models.CharField( max_length=2,
                           choices=PROPERTY_CHOICES,
                           default="HO")
    description = models.CharField( max_length=500)
    price = models.IntegerField(null=False,blank=False)
    area = models.FloatField()
    site = models.CharField( max_length=50)
    rating = models.IntegerField()
    n_bathroom = models.IntegerField()
    n_room = models.IntegerField()
    type_r = models.CharField( max_length=50)
    floor = models.CharField( max_length=50)
    n_bed = models.IntegerField()
    n_salon = models.IntegerField()
    furntiure = models.BooleanField(default=True)
    wifi = models.BooleanField(default=True)
    garden = models.BooleanField(default=True)
    pool = models.BooleanField(default=True)
    elevator = models.BooleanField(default=True)
    soloar_system = models.BooleanField(default=True)
    counter = models.IntegerField(default=0)
    owner = models.ForeignKey(Customers, on_delete=models.CASCADE)
    
    def __str__(self):
        return  str(self.owner)
    
   
    