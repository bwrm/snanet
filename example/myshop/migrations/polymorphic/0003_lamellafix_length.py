# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_auto_20181112_0630'),
    ]

    operations = [
        migrations.AddField(
            model_name='lamellafix',
            name='length',
            field=models.CharField(blank=True, max_length=25, verbose_name='Lamellas height'),
        ),
    ]