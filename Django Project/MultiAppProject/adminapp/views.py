from django.shortcuts import render
from myapp.models import *

# Create your views here.
def admin_home(request):
    data=Userinfo.objects.all()
    return render(request,'admin_home.html',{'data':data})