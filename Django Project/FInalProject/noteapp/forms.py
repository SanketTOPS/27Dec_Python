from django import forms
from .models import *


class UsersignupForm(forms.ModelForm):
    class Meta:
        model = Usersignup
        fields = "__all__"


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Usersignup
        fields = [
            "firstname",
            "lastname",
            "username",
            "password",
            "state",
            "city",
            "mobile",
            "pphoto",
        ]


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = "__all__"
