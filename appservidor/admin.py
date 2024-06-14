from django.contrib import admin
from .models import AutorDb,LibroDb

# Register your models here.
class LibroInLine(admin.TabularInline):
    model=LibroDb
    extra=1

class AutorAdmin(admin.ModelAdmin):
    fields= ["nombre","apellido","email"]
    list_display=["nombre","apellido","email"]
    inlines=[LibroInLine]

admin.site.register(AutorDb,AutorAdmin)

@admin.register(LibroDb)#otra forma de registrar con el decorador
class LibroAdmin(admin.ModelAdmin):
    fields = ["titulo","fecha_publica","autor_fk"]
    list_display=["titulo","fecha_publica"]