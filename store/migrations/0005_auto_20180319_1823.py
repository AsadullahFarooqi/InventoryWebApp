# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-19 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20180319_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreEmployers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('id_card_number', models.BigIntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('contact', models.BigIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employers', to='store.Store')),
            ],
            options={
                'verbose_name_plural': 'Employers',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='employersledger',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer_ledger', to='store.StoreEmployers'),
        ),
        migrations.DeleteModel(
            name='CompanyEmployers',
        ),
    ]