from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import custom_user

class createUserForm(ModelForm):
    class Meta:
        model =custom_user
        fields = ['name','username','email','password']
        

