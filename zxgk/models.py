import uuid

from django.db import models

# Create your models here.

# class Zxgk(models.Model):
from dzfy.models import Fyxx, Wzlx


class Fgxx(models.Model):
    fid = models.CharField(max_length=100, default=str(uuid.uuid4()).replace('-', ''))
    cbr = models.CharField(max_length=20, verbose_name='承办人')
    lxdh = models.CharField(max_length=11, null=True, verbose_name='联系电话')
    bgjl = models.TextField(verbose_name='变更记录', null=True)

    def __str__(self):
        return self.cbr

    class Meta:
        verbose_name = '法官信息'
        verbose_name_plural = '法官信息'

class Wzxx(models.Model):
    wid = models.CharField(max_length=100, default=str(uuid.uuid4()).replace('-', ''))
    FY_CHOICES = [(1, '达州市中级人民法院'), (2, '开源法院')]
    # fymc = models.IntegerField(max_length=50, choices=FY_CHOICES, verbose_name='法院名称')
    # LX_CHOICES = [(1, '执行动态'), (1, '法律法规'), ]
    # wzlx = models.IntegerField(max_length=30, choices=LX_CHOICES, verbose_name='文章类型')
    bt = models.CharField(max_length=200, verbose_name='标题')
    fbr = models.CharField(max_length=10, verbose_name='发布人')
    fbsj = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    nr = models.TextField(verbose_name='内容')
    fymc = models.ForeignKey(Fyxx, verbose_name='法院名称')
    wzlx = models.ForeignKey(Wzlx, verbose_name='文章类型')

    def __str__(self):
        return self.bt
    class Meta:
        verbose_name = '文章管理'
        verbose_name_plural = '文章管理'
        ordering = ['-fbsj']

