from django.contrib import admin

# Register your models here.
from .models import Preguntas, Respuestas

class RespuestasInline(admin.TabularInline):
    model = Respuestas

class PreguntasAdmin(admin.ModelAdmin):
    inlines = [RespuestasInline]

admin.site.register(Preguntas, PreguntasAdmin)
#admin.site.register(Respuestas)
