from django.contrib import admin

# Register your models here.
from ajxx.models import Ajxx
from cpws.models import Cpws
from dzfy.models import Fyxx, Wzlx
from zxgk.models import Wzxx, Fgxx

class BaseAdmin(admin.ModelAdmin):
    class Media:
        js = (

            '/static/ueditor/ueditor.config.js',
            '/static/ueditor/ueditor.all.js',
            '/static/ueditor/lang/zh-cn/zh-cn.js',
            '/static/ueditor/config.js',
        )


class WzxxAdmin(BaseAdmin):
    list_display = ('fymc', 'wzlx', 'bt', 'fbr', 'fbsj')
    search_fields = ['wzlx', 'bt', ]
    fields = ('fymc', 'wzlx', 'bt', 'fbr', 'nr')

admin.site.register(Wzxx, WzxxAdmin)

class AjxxAdmin(BaseAdmin):

    list_display = ('ah', 'ajly', 'lasj', 'fgxx')
    search_fields = ['ah']
    fields = ('fgxx', 'ah', 'ajly', 'lasj', 'ktsj', 'cbft', 'zxay', 'zxyj', 'zxyjwsbh',
              'sxfyjjg', 'sqzxbd', 'sxsj', 'zxyjws', 'lxqk')

admin.site.register(Ajxx, AjxxAdmin)


class FgxxAdmin(BaseAdmin):

    list_display = ('cbr', 'lxdh')
    search_fields = ['cbr']
    fields = ('cbr', 'lxdh', 'bgjl')

admin.site.register(Fgxx, FgxxAdmin)

class CpwsAdmin(BaseAdmin):
    list_display = ('ajxx', 'bt', 'fbsj', 'fbr')
    search_fields = ['ajxx', 'bt', ]
    fields = ('ajxx', 'bt', 'fbr', 'nr')

admin.site.register(Cpws, CpwsAdmin)

class FyxxAdmin(BaseAdmin):
    search_fields = ['name', ]

admin.site.register(Fyxx, FyxxAdmin)

class WzlxAdmin(BaseAdmin):
    search_fields = ['name', ]

admin.site.register(Wzlx, WzlxAdmin)