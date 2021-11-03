from django.urls import path, include
from . import views as avs
from django.conf.urls import url

app_name = 'access'

urlpatterns = [
    url(r'^$', avs.login, name='login'),
    url(r'^register/$', avs.register, name='register'),
    url(r'^homepage/$', avs.go_to_homepage, name='homepage'),
    url(r'^logout/$', avs.logout, name='logout'),
    path('activate/<uidb64>/<token>', avs.activate, name='activate'),
]