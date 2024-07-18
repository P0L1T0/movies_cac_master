from django.shortcuts import render
from .models import Movie
from flask import Flask , request as flask_rekest

# Create your views here.

def home(request):
    movies = Movie.objects.all()
    return render(request, 'catalogue/home.html',{'movies':movies})

def detail(request):   #   detalle
    movies = Movie.objects.all()
    return render(request, 'catalogue/detail.html',{'movies':movies})

