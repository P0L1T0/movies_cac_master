from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    acclaimed = models.BooleanField(null=True, verbose_name="Aclamada")
    image = models.ImageField(blank=True, null=True, verbose_name="Imagen", upload_to="movies")
    description = models.TextField(null=True, verbose_name="Descripción")
    """
    director = models.CharField(max_length=255, null=True, verbose_name="Director")
    writer = models.CharField(max_length=255, null=True, verbose_name="Escritor")
    year = models.DateTimeField(null=True, verbose_name="Año")
    genre = models.CharField(max_length=255, null=True, verbose_name="Genero")
    description = models.TextField(null=True, verbose_name="Descripción")
    duration = models.CharField(max_length=255, null=True, verbose_name="Diración")
    """
    movie_creation_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Fecha de creacion registro de película")
    movie_modification_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Fecha de modificación registro de película")
    
    def __str__(self) :
        return self.title
    
    class Meta:
        verbose_name = "película"
        verbose_name_plural = "películas"
        ordering = ["-movie_creation_date"]   #   Lo que hace esto es apilar los objetos y los ordena por ultima fecha de creación.
        