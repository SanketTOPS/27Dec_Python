from django.contrib import admin
from .models import *

# Register your models here.


class productData(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "name"]


class categoryData(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "pname", "qty", "price", "pphoto", "name"]


admin.site.register(products, productData)
admin.site.register(category, categoryData)
