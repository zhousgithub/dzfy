import uuid

from django.db import models

from zxgk.models import Fgxx


class Ajxx(models.Model):
    aid = models.CharField(max_length=100, default=str(uuid.uuid4()).replace('-', ''), editable=False)
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
    lxqk = models.TextField(max_length=500, null=True, verbose_name='履行情况')
    fgxx = models.OneToOneField(Fgxx, null=True, verbose_name='承办人')

    def __str__(self, verbose_name=''):
        return self.ah

    class Meta:
        ordering = ['-ktsj']
        verbose_name = '案件信息'
        verbose_name_plural = '案件信息'

