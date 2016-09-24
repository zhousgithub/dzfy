from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index.html', views.index),
    url(r'^ajcx.html', views.ajcx),
    url(r'^video/(?P<page>[0-9]+).html', views.videoList),
    url(r'^ktgg/(?P<page>[0-9]+).html', views.ktList, name='views.ktList'),
    url(r'^znxx/(?P<lx>[0-9]+)/(?P<page>[0-9]+).html', views.znList, name='views.znList'),
    url(r'^znxx/show/(?P<wid>[A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12}).html', views.znShow, name='zn.show'),
    # url(r'^sszn/(?P<page>[0-9]+).html', views.ssList),
    url(r'^video/show/(?P<tid>[A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12}).html', views.videoShow),
]