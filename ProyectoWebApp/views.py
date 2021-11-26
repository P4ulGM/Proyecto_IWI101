from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")

def tutoriales(request):
    return render(request, "ProyectoWebApp/tutoriales.html")

def blog(request):
    return render(request, "ProyectoWebApp/blog.html")

def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")

def whatsapp(request):
    return render(request, "ProyectoWebApp/whatsapp.html")

