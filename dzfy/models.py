from django.db import models

# Create your models here.

class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    age = models.IntegerField()

class Fyxx(models.Model):

    name = models.CharField(max_length=30, verbose_name='法院名称')

    class Meta:
        verbose_name = '法院名称'
        verbose_name_plural = '法院名称'

    def __str__(self):
        return self.name

class Wzlx(models.Model):

    name = models.CharField(max_length=20, verbose_name='文章类型')

    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = '文章类型'

    def __str__(self):
        return self.name

class Gjlb(models.Model):

    mc = models.CharField(max_length=20, verbose_name='干警类别名称')

    class Meta:
        verbose_name = '干警类别名称'
        verbose_name_plural = '干警类别名称'
        ordering = ['id']

    def __str__(self):
        return self.mc


class Gjxx(models.Model):

    gjlb = models.ForeignKey(Gjlb, verbose_name='干警类别名称', default='')
    xm = models.CharField(max_length=20, verbose_name='姓名', default='')
    zc = models.CharField(max_length=20, verbose_name='职称', default='')
    dh = models.CharField(max_length=13, verbose_name='电话', default='')
    imgurl = models.FileField(max_length=100, verbose_name='图片', upload_to='images/%Y%m%d/')
    # imgurls = models.FilePathField(max_length=100, verbose_name='图片地址')

    class Meta:
        verbose_name = '干警信息'
        verbose_name_plural = '干警信息'

    def __str__(self):
        return self.xm

    # def toJson(self):
    #     import json
    #     return json.dump(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))