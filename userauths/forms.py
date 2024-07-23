from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))
    
    class Meta: 
        model = User
        fields = ['email', 'password1', 'password2', 'username']