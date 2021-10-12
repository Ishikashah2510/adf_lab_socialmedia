from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
from datetime import date
from datetime import datetime
from . import user_object
from access.isValidPassword import *

# Create your views here.

x = 0


def login(request):
    global x

    request.session.set_expiry(300)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                cuser = users.objects.filter(Q(email=form.cleaned_data['email_']) | Q(username=form.cleaned_data['email_']))
                user_object.curr_user = cuser.get(password=form.cleaned_data['password_'])
                user_object.curr_user.is_user_authenticated(True)
                request.session['current_user'] = form.cleaned_data['email_']
                return go_to_homepage(request)
            except Exception as e:
                print(e)
                return render(request, 'access/login.html', {'form': form, 'message': 'Forgot your password?'})
        else:
            return render(request, 'access/login.html', {'form': form, 'message': 'Not cool'})
    else:
        form = LoginForm()

    if x == 1:
        message = 'Account created successfully!'
        x = 0
    return render(request, 'access/login.html', {'form': form, 'message': message})


def register(request):
    global x

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                okay, message = data_okay(form)
                if okay:
                    x = 1
                    return HttpResponseRedirect('/access/')
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

    try:
        q = users.objects.get(username=form.cleaned_data['username'])
        return False, 'username already exists'
    except:
        pass

    form.save()
    return True, 'okay'


def go_to_homepage(request):
    return render(request, 'home/homepage.html', {'obj': user_object.curr_user})


def logout(request):
    user_object.curr_user.is_user_authenticated(yes=False)
    request.session.flush()
    return login(request)
