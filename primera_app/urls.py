from django.urls import path, include
from rest_framework import routers
from primera_app import views

router = routers.DefaultRouter()

router.register(r'nacionalidad', views.NacionalidadViewSet)
router.register(r'autores', views.AutorViewSet)
router.register(r'comunas', views.ComunaViewSet)
router.register(r'direcciones', views.DireccionViewSet)
router.register(r'biblioteca', views.BibliotecaViewSet)
router.register(r'lector', views.LectorViewSet)
router.register(r'tipos_categorias', views.TipoCategoriaViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'libros', views.LibroViewSet)
router.register(r'prestamo', views.PrestamoViewSet)
urlpatterns = [
path('', include(router.urls)),
]