from django.conf.urls import url

from . import views

app_name = 'mecanicos'

urlpatterns = [
    url(r'^$', views.index, name='index'),
   # url(r'^/registro/$', views.vote, name='registro'),
]