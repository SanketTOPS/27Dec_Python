from django.db import models


# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=20)


class category(models.Model):
    pname = models.CharField(max_length=20)
    qty = models.IntegerField()
    price = models.IntegerField()
    pphoto = models.ImageField(upload_to="Products")
    name = models.ForeignKey(products, on_delete=models.CASCADE)
