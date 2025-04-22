from django import forms
from .models import *


class productForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ["price", "qty", "pphoto", "pname", "name"]
