from django.db import models


# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=255)
    address_01 = models.TextField()
    phone_01 = models.CharField(max_length=15)
