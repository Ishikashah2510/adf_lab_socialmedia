from django.urls import path, include
from . import views as hvs
from django.conf.urls import url

app_name = 'home'

urlpatterns = [
    url(r'^profile/$', hvs.profile_view, name='profile')
]