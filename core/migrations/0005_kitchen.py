# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 11:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170118_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('desc', models.CharField(max_length=100, verbose_name='Description')),
                ('l', models.IntegerField(verbose_name='Length')),
                ('b', models.IntegerField(verbose_name='Breadth')),
                ('h', models.IntegerField(verbose_name='Height')),
                ('base_price', models.IntegerField(verbose_name='Base Price')),
                ('min_change', models.IntegerField(default=20, verbose_name='Miniumum Change')),
                ('max_change', models.IntegerField(default=40, verbose_name='Maximum Change')),
                ('slug', models.SlugField(editable=False, max_length=200, null=True)),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Theme', to='core.KTheme')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
