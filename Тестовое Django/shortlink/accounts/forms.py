from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Username')
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = User
        fields = ('username',)
