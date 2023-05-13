from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'title': 'Enter your password, password can’t be too similar to your other personal information, must contain at least 8 characters, can’t be entirely numeric' }),
        help_text='',
    )

    password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password', 'title': 'Repeat your password'}),
        help_text='',
    )
    
    username = forms.CharField(
        label='Username',
        max_length=150,
        help_text='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'title': 'Enter your username'}),
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']