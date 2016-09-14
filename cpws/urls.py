from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [

    # url(r'^admin/', admin.site.urls),
    url(r'^index.html', views.index, name='index'),
    url(r'^edit.html', views.edit, name='edit'),
    url(r'^(?P<cid>[a-zA-Z0-9]+).html', views.show, name='views.show'),
    url(r'^ajlx_(?P<wslb>[0-9]+)/(?P<page>[0-9]+).html', views.list, name='views.list'),

]