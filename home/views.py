from django.shortcuts import render
from access.models import *


# Create your views here.


def profile_view(request):
    user = users.objects.get(email=request.session['curr_user'])
    return render(request, 'home/profile.html', {'user': user})


def update(request):
    pass
