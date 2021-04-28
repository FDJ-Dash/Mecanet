import json

from .models import Talleres
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.


class TalleresList(ListView):
    model = Talleres
    template_name = 'talleres/display-talleres.html'
    context_object_name = 'talleres'


class TalleresDetail(DetailView):
    model = Talleres


class TallerCreation(CreateView):
    model = Talleres
    success_url = reverse_lazy('talleres:talleres_view')
    fields = ['nombre', 'descripcion', 'url', 'thumb']


class TallerUpdate(UpdateView):
    model = Talleres
    success_url = reverse_lazy('talleres:talleres_view')
    fields = ['nombre', 'descripcion', 'url', 'thumb']


class TallerDelete(DeleteView):
    model = Talleres
    success_url = reverse_lazy('talleres:talleres_view')

"""
def talleres_view(request):
    talleres = Talleres.objects.all()
    context = {'talleres': talleres }
    return render(request, 'talleres/display-talleres.html', context)
"""
# raise 404 if i try to access manually to this url
# http://127.0.0.1:8000/talleres/cargar-contenido-clase/1


def cargar_taller(request, id):
    if request.is_ajax():
        taller = Talleres.objects.get(id=id)
        return HttpResponse(
            json.dumps({ 'nombre': taller.nombre,
                         'descripcion': taller.descripcion,
                         'url': taller.url }),
            content_type="application/json; charset=utf8"
        )
    else:
        raise Http404