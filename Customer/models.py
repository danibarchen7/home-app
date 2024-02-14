from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Customers(AbstractUser):
    BUIER = "BU"
    SALER = "SA"
    CHOICES = [
        (BUIER,"Buier"),
        (SALER,"Saler")
    ]
    phone = models.BigIntegerField(null=True,blank=True)
    email = models.EmailField(max_length=254,null=False,blank=False,unique=True)
    picture = models.ImageField(null=True,blank = True,upload_to='static/custome')
    user_type = models.CharField(max_length=2,
                                     choices=CHOICES,
                                     default=SALER
                                     )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)
    objects = CustomUserManager()
    def __str__(self):
        return self.email