from django.urls import path
from . import views
# from userauths import views


urlpatterns = [
    path('', views.index, name='index'),
    path('collections', views.collections, name='collections'),
    path('contacto', views.contact, name='contact'),
    path('journal', views.journal, name='journal'),
    path('men', views.men, name='men'),
    path('women', views.women, name='women'),
    path('carrito', views.carrito, name='carrito'),

]
