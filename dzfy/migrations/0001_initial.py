# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
