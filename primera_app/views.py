
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ComunaSerializer, NacionalidadSerializer, DireccionSerializer, AutorSerializer, BibliotecaSerializer, LectorSerializer, PrestamoSerializer, LibroSerializer, TipoCategoriaSerializer, CategoriaSerializer
from .models import Comuna, Nacionalidad, Direccion, Autor, Biblioteca, Lector, Prestamo, Libro, TipoCategoria, Categoria
# Create your views here.
def pagina_inicio(request):
    return render(request, 'primera_app/inicio.html')

class BibliotecaViewSet(viewsets.ModelViewSet): 
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer 

class NacionalidadViewSet(viewsets.ModelViewSet): 
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer

class ComunaViewSet(viewsets.ModelViewSet): 
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class AutorViewSet(viewsets.ModelViewSet): 
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class DireccionViewSet(viewsets.ModelViewSet): 
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class TipoCategoriaViewSet(viewsets.ModelViewSet):
    queryset = TipoCategoria.objects.all()
    serializer_class = TipoCategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer