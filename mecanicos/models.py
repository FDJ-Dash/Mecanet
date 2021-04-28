from django.db import models
# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    # Opcionales
    MASCULINO = 'M'
    FEMENINO = 'F'
    opciones_sexo = (
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    )
    sexo = models.CharField(
        max_length=1,
        choices=opciones_sexo,
        blank=True,
    )
    edad = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre


class Taller(models.Model):
    foto = models.ImageField(upload_to='talleres')
    descripcion = models.TextField(blank=True)
    email = models.EmailField(max_length=254, blank=True)
    website = models.URLField(max_length=300, blank=True)
    calificacion = models.PositiveSmallIntegerField()
    resenia = models.CharField(max_length=200)

    def __str__(self):
        return "Descripcion: %s " % self.descripcion

# las clases Ubicacion, Servicios y Resenia
# son extensiones de la clase taller por tal
# motivo la relacion es uno a uno.

class Ubicacion(models.Model):
    taller = models.OneToOneField(
        Taller,
        on_delete=models.CASCADE,
        primary_key=True)
    pais = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    mapa = models.URLField(max_length=200)

    def __str__(self):
        return "Ciudad: %s " % self.ciudad


class Servicios(models.Model):
    taller = models.OneToOneField(
        Taller,
        on_delete=models.CASCADE,
        primary_key=True)
    gomeria = models.BooleanField()
    balanceo = models.BooleanField()
    alineacion = models.BooleanField()
    chapa_y_pintura = models.BooleanField()

    def __str__(self):
        return "Servicios: "


class ReseniaUsuario(models.Model):
    taller = models.OneToOneField(
        Taller,
        on_delete=models.CASCADE,
        primary_key=True)
    usuario = models.ForeignKey(Usuario)
    resenia = models.CharField(max_length=200)

    def __str__(self):
        return "Reseña: %s " % self.resenia

