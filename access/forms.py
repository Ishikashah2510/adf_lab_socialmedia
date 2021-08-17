from django import forms
from .models import *
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class LoginForm(forms.Form):
    email_ = forms.EmailField(label=mark_safe('Email ID<br>'),
                              label_suffix='',
                              widget=forms.TextInput(attrs={'placeholder': 'johndoe@unknown.com',
                                                            'size': 30, 'style': 'height: 24px'}))
    password_ = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Top secret key here🤫',
                                                                                 'size': 26, 'style': 'height: 24px',
                                                                                 }),
                                label=mark_safe('Password<br>'),
                                label_suffix='')


class RegistrationForm(ModelForm):
    class Meta:
        model = users
        fields = '__all__'
        widgets = {
            'name': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
