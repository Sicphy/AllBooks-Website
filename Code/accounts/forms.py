from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):  
    class Meta:
        model = User
        fields = ('username', 'email')