from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.

def index(request):
    features=Feature.objects.all()

    return render(request,'index.html',{'Features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']

        if password == confirm_password:
          if User.objects.filter(email = email).exists():
             messages.info(request,'email already used')
             return redirect('register')
          elif User.objects.filter(username = username).exists():
            messages.info(request,'Username already used')
            return redirect('register')
          else:
            user = User.objects.create_user(username = username,email = email,password = password)
            user.save()
            return redirect('login')
        else:
            messages.info(request, 'Password are not same')
            return redirect('register')

    else:
        return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        passowrd=request.POST['password']

        user = auth.authenticate(username=username, password=passowrd)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Credentials Invalid")
            return redirect('login')  
    else:
        return render(request,'login.html')

def Logout(request):
    auth.logout(request)
    return redirect('/')


def counter(request):
    words=request.POST['words']
    
    return render(request,'counter.html',{'length': words })

