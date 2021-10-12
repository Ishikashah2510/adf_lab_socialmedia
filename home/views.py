from django.shortcuts import render
from access.models import *
from access import user_object

# Create your views here.


def profile_view(request):
    return render(request, 'home/profile.html', {'user': user_object.curr_user})


def update(request):
    pass
