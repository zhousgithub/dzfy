# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpws', '0003_auto_20160914_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpws',
            name='cid',
            field=models.CharField(default='dd5fe89ffcf4476c91adc59552455fa4', editable=False, max_length=100, verbose_name='cid'),
        ),
    ]