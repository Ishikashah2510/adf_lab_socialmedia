from django.db.models import Q
from django.shortcuts import render
from .models import *
from .forms import *
from datetime import date
from access.isValidPassword import *

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, 'home/homepage.html')
        else:
            return render(request, 'access/login.html', {'form': form, 'message': 'Not cool'})
    else:
        form = LoginForm()

    return render(request, 'access/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        try:
            if form.is_valid():
                okay, message = data_okay(form)
                if okay:
                    return render(request, 'access/login.html', {'message': 'Account created successfully!'})
                else:
                    return render(request, 'access/register.html', {'message': message, 'form': form})
        except Exception as e:
            print(e)
            return render(request, 'access/register.html', {'form': form, 'message': 'Data entered is invalid'})
    else:
        form = RegistrationForm()

    return render(request, 'access/register.html', {'form': form})


def data_okay(form):
    q1 = users.objects.filter(Q(email=form.cleaned_data['email']) | Q(mobile_no=form.cleaned_data['mobile_no']))
    if q1:
        return False, 'Account already exists'

    if form.cleaned_data['password'] != form.cleaned_data['repassword_']:
        return False, 'Passwords do not match'

    birthDate = form.cleaned_data['birthdate']
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    if age < 18:
        return False, 'Too young to join Connectify'

    if not isValidPassword(form.cleaned_data['password']):
        password_valid_string = '''Your password must contain
        at least 1 digit, 1 capital letter, 
        and at least one of _#!$%&*'''
        return False, password_valid_string

    form.save()
    return True