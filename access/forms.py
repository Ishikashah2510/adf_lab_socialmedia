from django import forms
from .models import *
from django.forms import ModelForm, BaseModelForm, BaseForm
from django.utils.safestring import mark_safe
import random


class LoginForm(forms.Form):
    email_ = forms.CharField(label=mark_safe('Unique ID<br>'),
                              help_text="<p style='font-size:14px'>You can enter your email ID or username</p>",
                              label_suffix='',
                              widget=forms.TextInput(attrs={'placeholder': 'johndoe@unknown.com or brickbreeder',
                                                            'size': 40, 'style': 'height: 24px'}))
    password_ = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Top secret key here🤫',
                                                                                 'size': 26, 'style': 'height: 24px',
                                                                                 }),
                                label=mark_safe('Password<br>'),
                                label_suffix='')


class RegistrationForm(ModelForm):
    class Meta:
        genders = [
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Others'),
            ('Not specified', 'Do not wish to specify')
        ]

        first_ = ['dragon', 'cupcake', 'burrito', 'hooman', 'brick']
        last_ = ['launcher', 'creator', 'thrower', 'breeder', 'manager']

        username_ = random.choice(first_) + random.choice(last_)

        model = users
        fields = '__all__'
        exclude = ('acc_creation_date', 'is_active', 'is_authenticated')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Jane Doe',
                                           'size': 26, 'style': 'height: 24px',},),
            'email': forms.TextInput(attrs={'placeholder': 'janedoe@incognito.com',
                                            'size': 26, 'style': 'height: 24px', }, ),
            'birthdate': forms.DateInput(attrs={'type':'date', 'required': True}),
            'gender': forms.Select(choices=genders),
            'mobile_no': forms.TextInput(attrs={'placeholder': '9182736450',
                                                'size': 26, 'style': 'height: 24px', }, ),
            'password': forms.PasswordInput(attrs={'placeholder': 'Open Sesame code',
                                               'size': 26, 'style': 'height: 24px', }, ),
            'username': forms.TextInput(attrs={'placeholder': username_,
                                               'size': 26, 'style': 'height: 24px'}),
            'pro_pic': forms.FileInput(attrs={'accept': 'image/*'})
        }

    repassword_ = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Re-type Open Sesame code',
                                                                                 'size': 26, 'style': 'height: 24px',
                                                                                 }),
                                  label=mark_safe('Re-enter password: '),
                                  label_suffix='')
