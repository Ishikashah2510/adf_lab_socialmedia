from django.shortcuts import render
from .forms import *

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, 'access/login.html', {'message': 'All cool'})
        else:
            return render(request, 'access/login.html', {'form': form, 'message': 'Not cool'})
    else:
        form = LoginForm()

    return render(request, 'access/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return render(request, 'access/register.html', {'message': 'All cool'})
        else:
            return render(request, 'access/register.html', {'form': form, 'message': 'Not cool'})
    else:
        form = RegistrationForm()

    return render(request, 'access/register.html', {'form': form})