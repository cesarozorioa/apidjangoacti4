from django.db import models

# Create your models here.
class AutorDb(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    class Meta:
        db_table = "Autores"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    def __str__(self):
        return self.nombre

class LibroDb(models.Model):
    titulo = models.CharField(max_length=50)
    fecha_publica = models.DateField(verbose_name="Fecha Publicacion",null=False)
    autor_fk = models.ForeignKey(AutorDb, on_delete=models.CASCADE,related_name='libros')
    class Meta:
        db_table = "Libros"
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
    def __str__(self):
        return self.titulo