from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    acclaimed = models.BooleanField(null=True)
    image = models.ImageField(blank=True, null=True)
    
    
    """_summary_
    
    director = models.CharField(max_length=255, null=True)
    writer = models.CharField(max_length=255, null=True)
    year = models.DateTimeField(null=True)
    genre = models.CharField(max_length=255, null=True)
    description = models.TextField()
    duration = models.CharField(max_length=255, null=True)
    acclaimed = models.BooleanField(null=True)
    image = models.ImageField(null=True)
    movie_creation_date = models.DateTimeField(auto_now_add=True, null=True)
    movie_modification_date = models.DateTimeField(auto_now=True, null=True)
    """