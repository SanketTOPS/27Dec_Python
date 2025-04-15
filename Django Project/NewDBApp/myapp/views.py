from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def index(request):
    msg = ""
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            print("Record Inserted!")
            msg = "Record Inserted!"
            # return redirect("/")
        else:
            print(form.errors)
            msg = "Error!"
    return render(request, "index.html", {"msg": msg})
