from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def collections(request):
    return render(request, 'core/collections.html')

def journal(request):
    return render(request, 'core/journal.html')

def men(request):
    return render(request, 'core/men.html')

def women(request):
    return render(request, 'core/women.html')

#register section
def accounts(request):
    return render(request, 'registration/login.html')

def accounts(request):
    return render(request, 'registration/register.html')

