from django.db import models

# Create your models here.
class Nacionalidad(models.Model):
    pais = models.CharField(max_length=50, null=False)
    nacionalidad = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_app = models.DateTimeField(auto_now_add=True)

class Autor(models.Model):
    nombre = models.CharField(max_length=250,null=False)
    pseudonimo = models.CharField(max_length=50, null=True)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    bio = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_app = models.DateTimeField(auto_now_add=True)

class Comuna(models.Model):
    codigo = models.CharField(max_length=5, null=False)
    comuna = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_app = models.DateTimeField(auto_now_add=True)

class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    calle = models.CharField(max_length=50, null=True)
    numero = models.CharField(max_length=20, null=True)
    departamento = models.CharField(max_length=10, null=True)
    detalles = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_app = models.DateTimeField(auto_now_add=True)

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=40, null=False)
    direccion = models.CharField(max_length=80, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_app = models.DateTimeField(auto_now_add=True)

class Libro(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    genero = models.CharField(max_length=15, null=False)
    titulo = models.CharField(max_length=40, null=False)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    paginas = models.CharField(max_length=700, null=False)
    copias = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_app = models.DateTimeField(auto_now_add=True)

class Lector(models.Model):
    nombre = models.CharField(max_length=60, null=False)
    rut = models.CharField(max_length=10, null=False)
    digito_verificador = models.CharField(max_length=1, null=False)
    correo = models.CharField(max_length=30, null=True)
    telefono = models.CharField(max_length=15, null=False)
    direccion = models.CharField(max_length=60, null=False)
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_app = models.DateTimeField(auto_now_add=True)

class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField
    fecha_devolucion = models.DateField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_app = models.DateTimeField(auto_now_add=True)