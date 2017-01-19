# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 11:22
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_wtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='WTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Theme Name')),
                ('desc', models.CharField(max_length=100, verbose_name='Description')),
                ('image', models.ImageField(upload_to='wardrobe/images/wardrobe_themes/')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('w_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='w_type', to='core.WType')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'core_wardrobe_theme',
                'verbose_name': 'Wardrobe Theme',
                'verbose_name_plural': 'Wardrobe Themes',
            },
        ),
        migrations.AlterUniqueTogether(
            name='wtheme',
            unique_together=set([('w_type', 'slug')]),
        ),
    ]
