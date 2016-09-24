from django.contrib import admin

# Register your models here.
from zxgk.models import Fgxx
from .models import Ajxx, Ajlx


class AjxxAdmin(admin.ModelAdmin):

    list_display = ('ah', 'ajly', 'lasj', 'fgxx')
    search_fields = ['ah']
    fields = ('ajlx', 'fgxx', 'ah', 'ajly', 'lasj', 'ktsj', 'cbft', 'zxay', 'zxyj', 'zxyjwsbh',
              'sxfyjjg', 'sqzxbd', 'sxsj', 'zxyjws', 'lxqk', 'aqjj')

admin.site.register(Ajxx, AjxxAdmin)

class AjlxAdmin(admin.ModelAdmin):
    search_fields = ['lx']

admin.site.register(Ajlx, AjlxAdmin)
