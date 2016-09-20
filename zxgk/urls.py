from django.conf.urls import url

from zxgk import views

urlpatterns = [

    url(r'^index.html', views.index, name='views.index'),
    url(r'^wzxx/(?P<wid>[0-9a-zA-Z]+).html', views.show, name='views.show'),
    url(r'^wzlx_(?P<id>[0-9]+)/(?P<page>[0-9]+).html', views.list, name='views.list'),
    url(r'^zxgk/(?P<page>[0-9]+).html', views.ajList, name='views.ajList'),
    url(r'^ajxq/(?P<aid>[a-zA-Z0-9]+).html', views.ajShow, name='views.ajShow'),
    url(r'^sxpg/(?P<page>[0-9]+).html', views.sxpg, name='views.ajShow'),

]