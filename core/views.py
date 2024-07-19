from django.shortcuts import render, redirect


from .models import Carrito, Cliente, Producto
from django.http import JsonResponse
from django.views import View

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

#Carrito 

def carrito(request):
    return render(request, 'core/carrito.html')

def add_carrito(request):
    user=request.user
    producto_id=request.GET.get('prod_id')
    producto = Producto.objects.get(id=producto_id)
    Carrito(user=user,producto=producto).save()
    return redirect("/carrito")

def mostrar_carrito(request):
    user = request.user
    carrito = carrito.objects.filter(user=user)
    monto = 0
    for p in carrito:
        valor = p.cantidad * p.producto.precio
        monto = monto + valor
    totalmonto = monto + 19
    return render(request, 'core/carrito.html',locals())

class checkout(View):
    def get(self,request):
        user=request.user
        add=Cliente.objects.filter(user=user)
        cart_items=Carrito.objects.filter(user=user)
        fmonto = 0
        for p in carrito:
            valor = p.cantidad * p.producto.precio
            fmonto = fmonto + valor
        totalmonto = fmonto + 19
        return render(request, 'core/carrito.html',locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id =request.GET['prod_id']
        c = Carrito.objects.get(Q(Producto=prod_id) & Q(user=request.user))
        c.cantidad+=1
        c.save()
        user = request.user
        carrito = Carrito.objects.filter(user=user)
        monto = 0
        for p in Carrito:
            valor = p.cantidad * p.producto.precio
            monto = monto + valor
        totalmonto = monto + 19
        data={
            'cantidad':c.cantidad,
            'monto':monto,
            'totalmonto':totalmonto
        }
        return JsonResponse(data)
    
def minus_cart(request):
    if request.method == 'GET':
        prod_id =request.GET['prod_id']
        c = Carrito.objects.get(Q(Producto=prod_id) & Q(user=request.user))
        c.cantidad+=1
        c.save()
        user = request.user
        carrito = Carrito.objects.filter(user=user)
        monto = 0
        for p in Carrito:
            valor = p.cantidad * p.producto.precio
            monto = monto + valor
        totalmonto = monto + 19
        data={
            'cantidad':c.cantidad,
            'monto':monto,
            'totalmonto':totalmonto
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id =request.GET['prod_id']
        c = Carrito.objects.get(Q(Producto=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        carrito = Carrito.objects.filter(user=user)
        monto = 0
        for p in Carrito:
            valor = p.cantidad * p.producto.precio
            monto = monto + valor
        totalmonto = monto + 19
        data={
            'cantidad':c.cantidad,
            'monto':monto,
            'totalmonto':totalmonto
        }
        return JsonResponse(data)

# #register section
# def accounts(view):
#     def get(self,request):
#         form = accountsForm()
#         return render(request, 'registration/login.html')
#     def post(self,request):
#         form = accountsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Felicidades! Usuario registrado exitoso")
#         else:
#             messages.warning(request,"datos invalidos")
#         return render(request, 'registration/login.html')


# def accounts(request):
#     return render(request, 'registration/register.html')

