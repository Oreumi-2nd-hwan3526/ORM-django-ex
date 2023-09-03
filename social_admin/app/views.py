from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def login_sucess(request):
    username = request.user
    return render(request, 'main.html', {'username': username})

def logout_view(request):
    logout(request)
    return redirect('login')