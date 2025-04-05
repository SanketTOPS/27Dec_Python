from django import forms
from .models import *


class studinfoForm(forms.ModelForm):
    class Meta:
        model = studinfo
        # fields=['name','email','mobile','dob','address']
        fields = "__all__"
