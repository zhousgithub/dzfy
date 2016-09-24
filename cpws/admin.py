from django.contrib import admin

# Register your models here.
from cpws.models import Cpws
from dzfy.admin import BaseAdmin


class CpwsAdmin(BaseAdmin):
    list_display = ('ajxx', 'bt', 'fbsj', 'fbr')
    search_fields = ['ajxx', 'bt', ]
    fields = ('fymc', 'ajxx', 'bt', 'fbr', 'nr')

admin.site.register(Cpws, CpwsAdmin)
