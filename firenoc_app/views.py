from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth

# Create your views here.

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                return render(request,'register.html')
            else:
                return render(request,'home.html')
                
    else:
        return render(request,'index.html')

def register(request):
    return render(request,'register.html')
