from django.urls import path
from core.views import index


app_name = "Ecommerce"

urlpatterns = [
    path("", index)
]
