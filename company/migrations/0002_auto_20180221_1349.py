# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-21 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]