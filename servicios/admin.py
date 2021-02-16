from django.contrib import admin
from .models import servicio

# Register your models here.

class servicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(servicio, servicioAdmin)