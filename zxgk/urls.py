from django.conf.urls import url

from zxgk import views

urlpatterns = [

    url(r'^index.html', views.index, name='views.index'),
    url(r'^wzxx/(?P<wid>[A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12}).html', views.show, name='views.show'),
    url(r'^wzlx_(?P<id>[0-9]+)/(?P<page>[0-9]+).html', views.list, name='views.list'),
    url(r'^zxgk/(?P<page>[0-9]+).html', views.ajList, name='zxgk.zxgk'),
    url(r'^ajxq/(?P<aid>[A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12}).html', views.ajShow, name='views.ajShow'),
    url(r'^sxpg/(?P<page>[0-9]+).html', views.sxpg, name='views.sxpg'),
    url(r'^sxgk/(?P<did>[A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12}).html', views.sxgk, name='views.sxgk'),
    url(r'^gjml/(?P<gjlb>[0-9]+).html', views.gjml, name='views.gjml'),
    url(r'^gjxx/(?P<gjlb>[0-9]+).html', views.gjxx, name='views.gjxx'),


]