from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [

    # url(r'^admin/', admin.site.urls),
    url(r'^index.html', views.index, name='index'),
    url(r'^edit.html', views.edit, name='edit'),
    url(r'^(?P<lx>[0-9]+)/(?P<cid>[A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12}).html', views.show, name='ws.show'),
    url(r'^ajlx_(?P<lx>[0-9]+)/(?P<page>[0-9]+).html', views.list, name='ws.list'),
    url(r'^byAjlx/(?P<lx>[0-9]+)$', views.byAjlx, name='ws.byAjlx'),

]