from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    phone_number= models.CharField(max_length=15, unique=True)
    address= models.CharField(max_length=255)
    pin_code=models.CharField(max_length=6)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    