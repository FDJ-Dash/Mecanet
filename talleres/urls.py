from django.conf.urls import url
from .views import (
    TalleresList,
    TalleresDetail,
    TallerCreation,
    TallerUpdate,
    TallerDelete,
    cargar_taller
)

app_name = 'talleres'
urlpatterns = [
    url(r'^talleres/$', TalleresList.as_view(), name='talleres_view'),
    url(r'cargar-contenido-taller/(?P<id>\d+)$', cargar_taller),
    url(r'^(?P<pk>\d+)$', TalleresDetail.as_view(), name='TalleresDetail'),
    url(r'^nuevo$', TallerCreation.as_view(), name='newTaller'),
    url(r'^editar/(?P<pk>\d+)$', TallerUpdate.as_view(), name='editTaller'),
    url(r'^borrar/(?P<pk>\d+)$', TallerDelete.as_view(), name='deleteTaller')
]