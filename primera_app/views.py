from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializer import ComunaSerializer, NacionalidadSerializer, DireccionSerializer, AutorSerializer, BibliotecaSerializer, LectorSerializer, PrestamoSerializer, LibroSerializer, TipoCategoriaSerializer, CategoriaSerializer
from .models import Comuna, Nacionalidad, Direccion, Autor, Biblioteca, Lector, Prestamo, Libro, TipoCategoria, Categoria
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('login')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso. ¡Bienvenido!")
        else:
            messages.error(
                request, "No ha sido posible Registrarlo. Por favor revise el formulario por errores."
            )
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def pagina_inicio(request):
    request.session['mensaje_bienvenida'] = '¡Bienvenido'
    mensaje_bienvenida = request.session.get('mensaje_bienvenida')
    if 'mensaje_bienvenida' in request.session:
        del request.session['mensaje_bienvenida']
    return render(request, 'primera_app/inicio.html',{'message': mensaje_bienvenida})

class BibliotecaViewSet(viewsets.ModelViewSet): 
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated] 

class NacionalidadViewSet(viewsets.ModelViewSet): 
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class ComunaViewSet(viewsets.ModelViewSet): 
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class AutorViewSet(viewsets.ModelViewSet): 
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class DireccionViewSet(viewsets.ModelViewSet): 
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class TipoCategoriaViewSet(viewsets.ModelViewSet):
    queryset = TipoCategoria.objects.all()
    serializer_class = TipoCategoriaSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]