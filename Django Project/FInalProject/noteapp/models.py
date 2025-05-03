from django.db import models

# Create your models here.


class Usersignup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    pphoto = models.ImageField(upload_to="ProfilePhoto")
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.EmailField()
    password = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
