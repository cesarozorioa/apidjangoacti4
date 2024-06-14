from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver#nos permite manejar señales
from .models import Perfil

@receiver(post_save, sender=Perfil)#se usa tratar las señales conrrespondietes
def add_user_to_comun_group(sender, instance, created,**kwargs):
    if created:
        try:
            administradores = Group.objects.get(name='Administradores')
        except Group.DoesNotExist:
            administradores = Group.objects.create(name='Administradores')
            administradores = Group.objects.create(name='Empleados')            
            
        instance.usuario.groups.add(administradores)
       
        
   