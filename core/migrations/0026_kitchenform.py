# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 07:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_wimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='KitchenForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=10)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.WColor')),
                ('finishing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.WFinishing')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.WMaterial')),
                ('wardrobe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Wardrobe')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]