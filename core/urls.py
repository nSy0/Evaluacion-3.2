from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('collections', views.collections, name='collections'),
    path('contacto', views.contacto, name='contacto'),
    path('journal', views.journal, name='journal'),
    path('men', views.men, name='men'),
    path('women', views.women, name='women'),
    path('carrito', views.carrito, name='carrito'),
    #register section
    path('login', views.accounts, name='login'),
    path('register', views.accounts, name='register'),
]
