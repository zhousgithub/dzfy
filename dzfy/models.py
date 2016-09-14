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