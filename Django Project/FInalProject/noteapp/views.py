from django.shortcuts import render
from .forms import *
from .models import *


# Create your views here.
def index(request):
    return render(request, "index.html")


def notes(request):
    return render(request, "notes.html")


def profile(request):
    return render(request, "profile.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        form = UsersignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Signup successfully!")
        else:
            print(form.errors)
    return render(request, "signup.html")
