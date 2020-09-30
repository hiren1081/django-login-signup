from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def intro(request):
    return render(request, "intro.html")


def home(request):
    return render(request, "home.html")


def signup(request):
    if (request.POST):
        login_data= request.POST.dict()
        username = login_data.get('username')
        password1 = login_data.get('pass1')
        password2 = login_data.get('pass2')
        # print(username, password1, password2)
        if(password1 == password2):
            
            user = User.objects.create_user(username=username, password=password2)
            print("user created successfully")
        else:
            print("password dose not match")
    return render(request, "signup.html")


def login_user(request):
    if request.GET:
        username = request.GET['username']
        password = request.GET['pass1']
        user = authenticate(request, username=username, password=password)
        if request.user.is_authenticated:
            login(request, user)
            return redirect("/home/")
    return render(request, "login.html")