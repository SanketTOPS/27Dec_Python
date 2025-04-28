from django import forms
from .models import *


class Userinfoform(forms.ModelForm):
    class Meta:
        model=Userinfo
        fields='__all__'