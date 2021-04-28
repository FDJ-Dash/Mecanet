from django.conf.urls import url

from . import views

app_name = 'comentarios'
urlpatterns = [
    url(r'^guardar-pregunta/$', views.guardar_pregunta, name='guardar_pregunta'),
    url(r'^cargar-respuestas/(?P<id>\d+)$', views.cargar_respuestas),
    url(r'^guardar-respuesta/$', views.guardar_respuesta),
]