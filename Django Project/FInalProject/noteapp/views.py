from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.core.mail import send_mail
import random
from FInalProject import settings


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
    msg = ""
    if request.method == "POST":
        form = UsersignupForm(request.POST, request.FILES)
        username = ""
        if form.is_valid():
            username = form.cleaned_data.get("username")
            try:
                Usersignup.objects.get(username=username)
                print("Username is already exists!")
                msg = "Username is already exists!"
            except Usersignup.DoesNotExist:
                form.save()
                print("Signup successfully!")
                msg = "Signup Successfully!"

                # Email Sending Code
                otp = random.randint(11111, 99999)
                send_mail(
                    subject="Your OTP Verification",
                    message=f"Dear User!\n\nThank you for registration with us!\nYour one time password is {otp}\n\nThanks & Regards!\nNotesApp\nTOPS Technologies\n+9724799469 | sanket.tops@gmail.com",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[request.POST["username"]],
                )
                return redirect("login")
        else:
            print(form.errors)
    return render(request, "signup.html", {"msg": msg})
