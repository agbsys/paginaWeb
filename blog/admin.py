from django.contrib import admin

# Register your models here.
from .models import categoria, post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(categoria, CategoriaAdmin)
admin.site.register(post, PostAdmin)