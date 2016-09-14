import uuid

from django.db import models

# Create your models here.
from ajxx.models import Ajxx


class Cpws(models.Model):

    cid = models.CharField(max_length=100, verbose_name='cid', default=str(uuid.uuid4()).replace('-', ''), editable=False)
    fymc = models.CharField(max_length=50, verbose_name='法院名称')
    bt = models.CharField(max_length=200, verbose_name='标题')
    fbr = models.CharField(max_length=10, verbose_name='发布人')
    fbsj = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    nr = models.TextField(verbose_name='内容')
    wslb = models.IntegerField(null=True, verbose_name='文书类型')#文书类型
    djl = models.IntegerField(default=1, verbose_name='点击量')#点击量
    ajxx = models.OneToOneField(Ajxx, null=True, verbose_name='案件信息')

    class Meta:
        ordering = ['-fbsj']
        verbose_name = '裁判文书'
        verbose_name_plural = '裁判文书'

    def __str__(self):
        return self.bt
