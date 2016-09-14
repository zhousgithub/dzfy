# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zxgk', '0005_auto_20160913_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fgxx',
            name='fid',
            field=models.CharField(default='fabfbe5fcaca401b804176051183e149', max_length=100),
        ),
        migrations.AlterField(
            model_name='wzxx',
            name='fymc',
            field=models.IntegerField(choices=[(1, '达州市中级人民法院'), (2, '开源法院')], max_length=50, verbose_name='法院名称'),
        ),
        migrations.AlterField(
            model_name='wzxx',
            name='wid',
            field=models.CharField(default='1fd8848306ee43e687019c42d4ed1af3', max_length=100),
        ),
        migrations.AlterField(
            model_name='wzxx',
            name='wzlx',
            field=models.IntegerField(choices=[(1, '执行动态'), (1, '法律法规')], max_length=30, verbose_name='文章类型'),
        ),
    ]
