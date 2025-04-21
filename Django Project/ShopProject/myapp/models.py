from django.db import models


# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class category(models.Model):
    pname = models.CharField(max_length=20)
    qty = models.IntegerField()
    price = models.IntegerField()
    pphoto = models.ImageField(upload_to="media/Products")
    name = models.ForeignKey(products, on_delete=models.CASCADE)
