from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    username = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(
        required=True, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(
        required=True, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists.')
        return email