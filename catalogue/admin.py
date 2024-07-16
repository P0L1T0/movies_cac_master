from django.contrib import admin
from .models import Movie


class ProjectCatalogue(admin.ModelAdmin):
    readonly_fields = ('movie_creation_date', 'movie_modification_date')

# Register your models here.

admin.site.register(Movie, ProjectCatalogue)
