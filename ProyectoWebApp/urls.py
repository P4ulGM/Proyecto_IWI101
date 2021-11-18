from django.urls import path

from ProyectoWebApp import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('blog',views.blog, name="Blog"),
    path('servicios',views.blog, name="Servicios"),
    path('contacto',views.contacto, name="Contacto"),

]