from django.contrib import admin
from .models import Producto, ImagenProducto , Contactoform

from django.contrib import admin

class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1
    max_num = 6  # Límite en el admin

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    inlines = [ImagenProductoInline]

@admin.register(Contactoform)
class ContactoformAdmin(admin.ModelAdmin): 
    pass
