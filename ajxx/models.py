import uuid

from django.db import models

from zxgk.models import Fgxx

class Ajlx(models.Model):

    lx = models.CharField(max_length=20, verbose_name='案件类型')

    class Meta:
        verbose_name = '案件类型'
        verbose_name_plural = '案件类型'

    def __str__(self):
        return self.lx

class Ajxx(models.Model):
    aid = models.UUIDField(max_length=100, default=uuid.uuid1, editable=False)
    ah = models.CharField(max_length=50, verbose_name='案号')
    cbfy = models.CharField(max_length=30, verbose_name='承办法院', null=True)
    ajly = models.CharField(max_length=50, null=True, verbose_name='案件来源')#案件来源
    lasj = models.DateTimeField(verbose_name='立案时间')
    ktsj = models.DateTimeField(null=True, verbose_name='开庭时间')
    cbft = models.CharField(max_length=50, null=True, verbose_name='承办法庭')#?承办法庭
    zxay = models.TextField(max_length=500, null=True, verbose_name='执行案由')#执行案由
    zxyj = models.TextField(max_length=500, null=True, verbose_name='执行依据')#执行依据
    zxyjwsbh = models.CharField(max_length=200, null=True, verbose_name='文书编号')#文书编号
    sxfyjjg = models.CharField(max_length=100, null=True, verbose_name='生效法院及机关')#生效判决法院及其它机关
    sqzxbd = models.FloatField(null=True, verbose_name='申请执行标的')
    sxsj = models.DateTimeField(null=True, verbose_name='生效时间')
    zxyjws = models.TextField(null=True, verbose_name='执行依据文书')
    lxqk = models.TextField(max_length=200, null=True, verbose_name='履行情况')
    fgxx = models.ForeignKey(Fgxx, null=True, verbose_name='承办人')
    aqjj = models.TextField(max_length=500, default='', null=True, verbose_name='案情简介')
    ajlx = models.ForeignKey(Ajlx, null=True, verbose_name='案件类型')

    class Meta:
        ordering = ['-ktsj']
        verbose_name = '案件信息'
        verbose_name_plural = '案件信息'

    def __str__(self, verbose_name=''):
        return self.ah


