from django.db import models

# Create your models here.


class Preguntas(models.Model):
    titulo = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo


class Respuestas(models.Model):
    titulo = models.CharField(max_length=255)
    pregunta = models.ForeignKey(Preguntas)

    def __str__(self):
        return ("Responde a: " + self.pregunta.titulo + ", respuesta: " + self.titulo)