from django.contrib import admin

# Register your models here.
from ajxx.models import Ajxx
from cpws.models import Cpws
from dzfy.models import Fyxx, Wzlx
from zxgk.models import Wzxx, Fgxx


class WzxxAdmin(admin.ModelAdmin):
    list_display = ('fymc', 'wzlx', 'bt', 'fbr', 'fbsj')
    search_fields = ['wzlx', 'bt', ]
    fields = ('fymc', 'wzlx', 'bt', 'fbr', 'nr')

admin.site.register(Wzxx, WzxxAdmin)

class AjxxAdmin(admin.ModelAdmin):

    list_display = ('ah', 'ajly', 'lasj', 'fgxx')
    search_fields = ['ah']
    fields = ('fgxx', 'ah', 'ajly', 'lasj', 'ktsj', 'cbft', 'zxay', 'zxyj', 'zxyjwsbh',
              'sxfyjjg', 'sqzxbd', 'sxsj', 'zxyjws', 'lxqk')

admin.site.register(Ajxx, AjxxAdmin)


class FgxxAdmin(admin.ModelAdmin):

    list_display = ('cbr', 'lxdh')
    search_fields = ['cbr']
    fields = ('cbr', 'lxdh', 'bgjl')

admin.site.register(Fgxx, FgxxAdmin)

class CpwsAdmin(admin.ModelAdmin):
    list_display = ('ajxx', 'bt', 'fbsj', 'fbr')
    search_fields = ['ajxx', 'bt',]
    fields = ('ajxx', 'bt', 'fbr', 'nr')

admin.site.register(Cpws, CpwsAdmin)

class FyxxAdmin(admin.ModelAdmin):
    search_fields = ['name', ]

admin.site.register(Fyxx, FyxxAdmin)

class WzlxAdmin(admin.ModelAdmin):
    search_fields = ['name', ]

admin.site.register(Wzlx, WzlxAdmin)