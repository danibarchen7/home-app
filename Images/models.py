from django.db import models

# Create your models here.
class images(models.Model):
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
        