from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Perfil (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,related_name='perfil',verbose_name='Usuario')
    image = models.ImageField(default='users/usuario_defecto.jpg',upload_to='users/',verbose_name='Imagen de perfil')
    direccion = models.CharField(max_length=100,null=True,blank=True,verbose_name='Direccion')
    telefono = models.CharField(max_length=10,null=True,blank=True,verbose_name='Telefono')
    class Meta:
        verbose_name='perfil'
        verbose_name_plural='perfiles'
        ordering = ['-id']
    
    def __str__(self):
        return self.usuario.username

#cuando se crea el usuario se crea el perfil
@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
        
#funcion cuando se grabe el perfil se grabe en al base de datos de perfiles
@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()