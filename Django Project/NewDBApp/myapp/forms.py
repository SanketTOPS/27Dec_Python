from django import forms
from .models import *


class userForm(forms.ModelForm):
    class Meta:
        model = userinfo
        fields = "__all__"


class updateuserForm(forms.ModelForm):
    class Meta:
        model = userinfo
        fields = ["name", "email", "mobile", "dob", "address"]
