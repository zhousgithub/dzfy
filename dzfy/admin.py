from django.contrib import admin

# Register your models here.
from ajxx.models import Ajxx
from cpws.models import Cpws
from dzfy.models import Fyxx, Wzlx, Gjxx, Gjlb
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

class FgxxAdmin(BaseAdmin):

    list_display = ('cbr', 'lxdh')
    search_fields = ['cbr']
    fields = ('cbr', 'lxdh', 'bgjl')

admin.site.register(Fgxx, FgxxAdmin)


class FyxxAdmin(BaseAdmin):
    search_fields = ['name', ]

admin.site.register(Fyxx, FyxxAdmin)

class WzlxAdmin(BaseAdmin):
    search_fields = ['name', ]

admin.site.register(Wzlx, WzlxAdmin)


class GjlbAdmin(BaseAdmin):

    search_fields = ['mc', ]
admin.site.register(Gjlb, GjlbAdmin)

class GjxxAdmin(BaseAdmin):
    list_display = ('gjlb', 'xm', 'zc', 'dh')
    search_fields = ['xm', 'zc']

    # def queryset(self, request):
    #     qs = super(GjxxAdmin, self).queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(uploader=request.user)

admin.site.register(Gjxx, GjxxAdmin)