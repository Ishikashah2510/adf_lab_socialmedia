from django import forms
from access.models import *


class UpdateForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ('username', 'mobile_no')
