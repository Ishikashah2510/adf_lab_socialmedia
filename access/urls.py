from . import views as avs
from django.conf.urls import url

app_name = 'access'

urlpatterns = [
    url(r'^$', avs.login, name='login'),
    url(r'^register/$', avs.register, name='register')
]