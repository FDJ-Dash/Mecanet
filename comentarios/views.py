import json

from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, Http404
from .models import Preguntas, Respuestas

def show_preguntas():
    preguntas = Preguntas.objects.all().order_by('-id')
    context = {'preguntas': preguntas}
    return context


@csrf_protect
def guardar_pregunta(request):
    if request.is_ajax():
        if request.POST['pregunta']:
            pregunta = Preguntas(titulo=request.POST['pregunta'])
            pregunta.save()

        preguntas = Preguntas.objects.all().order_by('-id')

        data = list()
        for pregunta in preguntas:
            data.append({'id': pregunta.id, 'titulo': pregunta.titulo})
        # serializo los datos con json para ajax
        return HttpResponse(
            json.dumps({'preguntas': data}),
            content_type="application/json; charset=utf8"
        )
    else:
        raise Http404


def cargar_respuestas(request, id):
    if request.is_ajax():
        respuestas = Respuestas.objects.filter(pregunta__id= id).order_by('-id')

        data = list()
        for respuesta in respuestas:
            data.append(respuesta.titulo)

        return HttpResponse(
            json.dumps({'respuestas': data, 'pregunta': id}),
            content_type="application/json; charset=utf8"
        )
    else:
        raise Http404


def guardar_respuesta(request):
    if request.is_ajax():
        if request.POST['respuesta']:
            respuesta = Respuestas(titulo= request.POST['respuesta'],
                                   pregunta_id= request.POST['pregunta'])
            respuesta.save()

        return cargar_respuestas(request, request.POST['pregunta'])