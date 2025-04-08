from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def index(request):
    if request.method == "POST":
        form = studinfoForm(request.POST)
        if form.is_valid():
            form.save()
            print("Data inserted!")
            return redirect("/")
        else:
            print(form.errors)
    return render(request, "index.html")


def showdata(request):
    stdata = studinfo.objects.all()
    return render(request, "showdata.html", {"stdata": stdata})


def update(request, id):
    stid = studinfo.objects.get(id=id)
    print("ID:", stid)
    if request.method == "POST":
        form = updateForm(request.POST, instance=stid)
        if form.is_valid():
            form.save()
            print("Record updated!")
            return redirect("showdata")
        else:
            print(form.errors)
    return render(request, "update.html", {"stid": stid})
