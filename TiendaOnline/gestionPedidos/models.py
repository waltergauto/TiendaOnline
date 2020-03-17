from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 50, verbose_name = "La Dirección") # el parámetro verbose_name sirve para indicarle al Django cómo queremos ver el atributo en el servidor
    email = models.EmailField(blank = True, null = True) #los argumentos blank y null son para hacer que el campo email sea opcional
    telefono = models.CharField(max_length = 10)

    def __str__(self): #con este metodo le decimos a django que queremos ver solo los nombres de los clientes, no como Object....
        return self.nombre

class Articulos(models.Model):
    nombre = models.CharField(max_length = 30)
    seccion = models.CharField(max_length = 20)
    precio = models.IntegerField()

    def __str__(self):
        return 'El nombre es %s, la sección es %s y el precio es %s' % (self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()