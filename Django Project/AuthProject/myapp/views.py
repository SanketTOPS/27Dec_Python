from django.shortcuts import render
from .forms import *


# Create your views here.
def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            print("Signup Successfully!")
        else:
            print(form.errors)
    return render(request, "signup.html")
