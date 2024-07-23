from django.urls import path
from userauths import views
from .views import contact_view, contact_success




urlpatterns = [
    
    path("sign-up/", views.register_view, name="sign-up"),
    path("sign-in/", views.login_view, name="sign-in"),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
]
