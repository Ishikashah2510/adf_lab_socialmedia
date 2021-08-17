from . import views as avs
from django.conf.urls import url

app_name = 'access'

urlpatterns = [
    url('', avs.login, name='login'),
    url('register', avs.register, name='register')
]