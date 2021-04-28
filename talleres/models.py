from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
class Talleres(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    url = models.CharField(max_length=100)
    thumb = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre