#from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Comuna_Serializer, Nacionalidad_Serializer, Direccion_Serializer, Autor_Serializer, Biblioteca_Serializer, Lector_Serializer, Prestamo_Serializer, Libro_Serializer
from .models import Comuna, Nacionalidad, Direccion, Autor, Biblioteca, Lector, Prestamo, Libro
# Create your views here.
class Biblioteca_ViewSet(viewsets.ModelViewSet): 
    queryset = Biblioteca.objects.all()
    serializer_class = Biblioteca_Serializer 

class Nacionalidad_ViewSet(viewsets.ModelViewSet): 
    queryset = Nacionalidad.objects.all()
    serializer_class = Nacionalidad_Serializer

class Comuna_ViewSet(viewsets.ModelViewSet): 
    queryset = Comuna.objects.all()
    serializer_class = Comuna_Serializer

class Autor_ViewSet(viewsets.ModelViewSet): 
    queryset = Autor.objects.all()
    serializer_class = Autor_Serializer

class Direccion_ViewSet(viewsets.ModelViewSet): 
    queryset = Direccion.objects.all()
    serializer_class = Direccion_Serializer

class Lector_ViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = Lector_Serializer

class Prestamo_ViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = Prestamo_Serializer

class Libro_ViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = Prestamo_Serializer