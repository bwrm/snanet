# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-18 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0008_auto_20181115_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='lamellafix',
            name='depth',
            field=models.CharField(blank=True, max_length=25, verbose_name="Lamella's depth"),
        ),
    ]