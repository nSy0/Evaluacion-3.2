from django.contrib import admin
from .models import Producto, Cliente, Carrito, Payment

# Register your models here.

@admin.register(Producto)
class ProductoModelAdmin(admin.ModelAdmin):
    list_display = ['id','titulo','precio','categoria','imagen_producto']

@admin.register(Cliente)
class ClienteModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','localidad','ciudad','comuna','telefono']

@admin.register(Carrito)
class CarritoModelAdmin(admin.ModelAdmin):
    list_display =['id','user','producto','cantidad']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display =['id','user','monto','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

