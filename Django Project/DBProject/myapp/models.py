from django.db import models


# Create your models here.
class studinfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    dob = models.DateField()
    address = models.TextField()
