from django.db import models

# Create your models here.
class Tipe(models.Model):
    tipe = models.CharField(max_length=50)