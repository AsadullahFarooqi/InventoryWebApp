# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-19 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20180319_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeemployers',
            name='position',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]