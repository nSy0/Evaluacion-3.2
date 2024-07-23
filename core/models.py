from django.db import models
# from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

#class User(AbstractBaseUser):
  #  email = models.EmailField(unique=True)
  #  username = models.CharField(max_length=100)

 #   USERNAME_FIELD = "email"
 #   REQUIRED_FIELDS = ['username']

   # def __str__(self):
   #     return self.username



class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.TextField()
    categoria = models.CharField( max_length=50)
    imagen_producto = models.ImageField(upload_to='producto')
    def __str__(self):
        return self.titulo

class Cliente(models.Model):
    user = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=50)
    telefono = models.IntegerField(default=0)
    comuna = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    user = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    @property
    def total_costo(self):
        return self.cantidad * self.producto

class Payment(models.Model):
    user = models.CharField(max_length=100)
    monto = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)
    


