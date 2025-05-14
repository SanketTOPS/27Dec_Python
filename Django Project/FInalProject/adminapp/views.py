from django.shortcuts import render, redirect
from noteapp.models import *

# Create your views here.


def admin_index(request):
    if request.method == "POST":
        username = "admin"
        password = "admin@123"

        unm = request.POST["username"]
        pas = request.POST["password"]

        if username == unm and password == pas:
            print("Login Successfully!")
            return redirect("admin_home")
        else:
            print("Error!Login faild...")
    return render(request, "admin_index.html")


def admin_home(request):
    return render(request, "admin_home.html")


def admin_userinfo(request):
    userdata = Usersignup.objects.all()
    return render(request, "admin_userinfo.html", {"userdata": userdata})


def admin_notesinfo(request):
    notesdata = Notes.objects.all()
    return render(request, "admin_notesinfo.html", {"notesdata": notesdata})
