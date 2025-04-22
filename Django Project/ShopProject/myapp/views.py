from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def index(request):
    data = category.objects.all()
    return render(request, "index.html", {"data": data})


def addproduct(request):
    data = category.objects.all()
    if request.method == "POST":
        form = productForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Product added!")
            return redirect("/")
        else:
            print(form.errors)
    return render(request, "addproduct.html", {"data": data})
