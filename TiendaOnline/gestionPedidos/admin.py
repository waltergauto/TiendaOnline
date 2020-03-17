from django.contrib import admin

from gestionPedidos.models import Cliente, Articulos, Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin): #esta clase se crea para poder decirle a Django qué cosas quiero ver de los clientes en el servidor
    list_display = ("nombre", "direccion")# en este caso se pone para ver nombre de Cliente y direccion de Cliente
    search_fields = ["nombre"] #agrega al panel de la tabla Cliente un buscador por nombre

admin.site.register(Cliente, ClientesAdmin) #al hacer la clase ClientesAdmin, esta linea tambien la debe de recibir como parametro
admin.site.register(Articulos)
admin.site.register(Pedidos)

