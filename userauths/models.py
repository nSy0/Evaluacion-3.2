from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username



#contact

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
    
class EntradaJournal(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateField()
    imagen_perfume = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.titulo