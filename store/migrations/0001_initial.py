# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-25 05:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContainersTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('approximate_weight_container_holds', models.PositiveIntegerField(blank=True, help_text='Make sure the value is in kg!', null=True)),
                ('length', models.PositiveIntegerField(blank=True, help_text='Make sure the value is in inches!', null=True)),
                ('width', models.PositiveIntegerField(blank=True, help_text='Make sure the value is in inches!', null=True)),
                ('depth', models.PositiveIntegerField(blank=True, help_text='Make sure the value is in inches!', null=True)),
                ('material_container_made_of', models.CharField(blank=True, max_length=50, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Types of Containers',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('id_card_number', models.BigIntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('contact', models.BigIntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Customers',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Exported',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_recipt_number', models.BigIntegerField(blank=True, null=True)),
                ('truck_plate_number', models.IntegerField(blank=True, null=True)),
                ('number_of_containers', models.IntegerField()),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('price_of_singal_item', models.IntegerField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('date', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Exports',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Imported',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_recipt_number', models.BigIntegerField()),
                ('truck_plate_number', models.IntegerField()),
                ('number_of_containers', models.IntegerField()),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('price_of_singal_item', models.IntegerField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('date', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Imports',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='PaymentsOfCustomers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_payments', to='store.Customer')),
            ],
            options={
                'verbose_name_plural': 'Payments OF Customers',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='PaymentsToSuppliers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Payments To Suppliers',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('details', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('capacity', models.PositiveIntegerField(blank=True, help_text='containers the store can hold', null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('store_is_active_from', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='company.Company')),
            ],
            options={
                'verbose_name_plural': 'Stores',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('id_card_number', models.BigIntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('contact', models.BigIntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='store.Store')),
            ],
            options={
                'verbose_name_plural': 'Suppliers',
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='products',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.Store'),
        ),
        migrations.AddField(
            model_name='paymentstosuppliers',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_import_payments', to='store.Store'),
        ),
        migrations.AddField(
            model_name='paymentstosuppliers',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_payments', to='store.Supplier'),
        ),
        migrations.AddField(
            model_name='paymentsofcustomers',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_export_payments', to='store.Store'),
        ),
        migrations.AddField(
            model_name='imported',
            name='containers_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_imports', to='store.Products'),
        ),
        migrations.AddField(
            model_name='imported',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_imports', to='store.Store'),
        ),
        migrations.AddField(
            model_name='imported',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_imports', to='store.Supplier'),
        ),
        migrations.AddField(
            model_name='imported',
            name='type_of_containers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contaner_type_imports', to='store.ContainersTypes'),
        ),
        migrations.AddField(
            model_name='exported',
            name='containers_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_exports', to='store.Products'),
        ),
        migrations.AddField(
            model_name='exported',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_exports', to='store.Customer'),
        ),
        migrations.AddField(
            model_name='exported',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_exports', to='store.Store'),
        ),
        migrations.AddField(
            model_name='exported',
            name='type_of_containers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contaner_type_exports', to='store.ContainersTypes'),
        ),
        migrations.AddField(
            model_name='customer',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='store.Store'),
        ),
        migrations.AddField(
            model_name='containerstypes',
            name='container_use_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contianer_types', to='store.Products'),
        ),
        migrations.AddField(
            model_name='containerstypes',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types_of_containers', to='store.Store'),
        ),
    ]
