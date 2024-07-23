from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User
from django.contrib.auth import get_user_model
from userauths.models import ContactMessage

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))
    
    class Meta: 
        model = User
        fields = ['email', 'password1', 'password2', 'username']
        
        


#contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not '@' in email:
            raise forms.ValidationError('Por favor, introduce un correo electrónico válido.')
        return email

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if len(subject) < 5:
            raise forms.ValidationError('El asunto debe tener al menos 5 caracteres.')
        return subject

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError('El mensaje debe tener al menos 10 caracteres.')
        return message