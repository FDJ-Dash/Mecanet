from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^phpinfo/$', views.php_view, name='php_view'),
    url(r'^login/$', views.enter, name='enter'),
    url(r'^logout/$', views.log_out, name='log_out'),
    url(r'^aboutfts/$', views.about_fts, name='about_fts'),
]