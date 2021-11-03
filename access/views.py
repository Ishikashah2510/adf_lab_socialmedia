from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from adf_lab_socialmedia import settings
from .forms import *
from datetime import date
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage, send_mail
from access.isValidPassword import *
from .tokens import generate_token

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
                cuser = cuser.get(password=form.cleaned_data['password_'])
                if cuser.is_active == True:
                    cuser.is_authenticated = True
                    cuser.save()
                    request.session['curr_user'] = form.cleaned_data['email_']
                    return go_to_homepage(request)
                else:
                    return render(request, 'access/login.html',
                                  {'form': form, 'message': 'havent authenticated yourself?',})
            except Exception as e:
                print(e)
                return render(request, 'access/login.html',
                              {'form': form, 'message': 'Forgot your password?'})
        else:
            return render(request, 'access/login.html', {'form': form, 'message': 'Not cool'})
    else:
        form = LoginForm()

    message = ''
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
                send_mail_(request, form.cleaned_data['email'])
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


def send_mail_(request, email):
    myuser = users.objects.get(email=email)
    current_site = get_current_site(request)
    email_subject = "Confirm your Email at Connectify"
    message2 = render_to_string('access/email_activation.html', {
        'name': myuser.name,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        'token': generate_token.make_token(myuser)
    })
    send_mail(email_subject, message2, settings.EMAIL_HOST_USER,
              recipient_list=[myuser.email], html_message=message2)


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
    user = users.objects.get(Q(email=request.session['curr_user']) | Q(username=request.session['curr_user']))
    return render(request, 'home/homepage.html', {'obj': user})


def logout(request):
    user = users.objects.get(email=request.session['curr_user'])
    user.user_authenticated = False
    request.session.flush()
    return HttpResponseRedirect('/access/')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = users.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,users.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request)
        messages.success(request, "Your Account has been activated!!")
        return redirect('/access/')
    else:
        return render(request,'activation_failed.html')
