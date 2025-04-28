from django.db import models

# Create your models here.

class Userinfo(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.DateField()
    mobile=models.BigIntegerField()
    city=models.CharField(max_length=20)