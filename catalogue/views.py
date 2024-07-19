from django.shortcuts import get_object_or_404, render
from .models import Movie

# Create your views here.

def home(request):
    movies = Movie.objects.all()
    return render(request, 'catalogue/home.html',{'movies':movies})

def detail(request):   #   detalle
    movies = Movie.objects.all()
    return render(request, 'catalogue/detail.html',{'movies':movies})
