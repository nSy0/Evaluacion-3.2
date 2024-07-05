from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from core import views


# Create your views here.

def index(request):
    return render(request, 'core/index.html')

