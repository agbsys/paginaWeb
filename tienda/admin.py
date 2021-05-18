from django.contrib import admin

# Register your models here.
from .models import categoriaProd, Productos

# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(categoriaProd, CategoriaProdAdmin)
admin.site.register(Productos, ProductosAdmin)