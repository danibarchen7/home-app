from django.db import models
from Type.models import Tipe
# Create your models here.
class Properties(models.Model):
    idt = models.ForeignKey(Tipe, on_delete=models.CASCADE)
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
    