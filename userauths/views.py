from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import ContactForm
from django.conf import settings
from .models import EntradaJournal

User = settings.AUTH_USER_MODEL

User = get_user_model()

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, tu cuenta fue creada exitosamente")
            
            # Autenticación del usuario
            new_user = authenticate(username=form.cleaned_data.get('username'),
                                    password=form.cleaned_data['password1'])
            if new_user is not None:
                login(request, new_user)
                return redirect("core:index")
            else:
                pass

    else:
        form = UserRegisterForm()
        
    context = {
        'form': form
    }
    return render(request, "userauths/sign-up.html", context)

#login

def login_view(request):
    if request.user.is_authenticated:
        # return redirect("core:index")
        pass
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request, f"Usuario con correo: {email} no existe.")
            
        user = authenticate(request, email = email, password = password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Has iniciado sesión.")
            # return redirect("core:index")
        else:
            messages.warning(request, "Este usuario no exite, cree una cuenta nueva.")
            
    context={}
            
    return render(request, "userauths/sign-in.html", context)
         

#contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'userauths/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'userauths/contact_success.html')





def journal(request):
    entradas = EntradaJournal.objects.all()
    print(entradas)  # Imprime las entradas en la consola para depuración
    return render(request, 'userauths/journal.html', {'entradas': entradas})
