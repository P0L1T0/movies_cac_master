from django.shortcuts import render, HttpResponse

# Create your views here.
    
def login(request):   #   inicio de sesión 
    return render(request, 'core/login.html')
    
def signup(request):   #   registrarse
    return render(request, 'core/signup.html')
    