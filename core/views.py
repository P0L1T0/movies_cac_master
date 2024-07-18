from django.shortcuts import render, HttpResponse

# Create your views here.
    
def detail(request):   #   detalle
    return render(request, 'core/detail.html')
    
def login(request):   #   inicio de sesión 
    return render(request, 'core/login.html')
    
def signup(request):   #   registrarse
    return render(request, 'core/signup.html')
    