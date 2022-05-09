from django import views
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from matplotlib.style import context
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, "index.html")

def createUser(request):
    form  = CustomUserCreationForm()
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            redirect('create_profile')
        
        else:
            print("Failed")

    context = {'form':form}

    return render(request, "users/signup.html", context)

def createProfile(request):
    context = {}
    return render(request, 'users/profile-form.html', context)
