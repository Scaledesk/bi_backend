# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 07:52
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KAppliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='kitchen/images/kitchen_appliances/')),
            ],
            options={
                'ordering': ('name', 'kitchen'),
                'db_table': 'core_kitchen_appliance',
                'verbose_name': 'Kitchen Apliance',
                'verbose_name_plural': 'Kitchen Appliances',
            },
        ),
        migrations.CreateModel(
            name='KColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('image', models.ImageField(upload_to='kitchen/images/kitchen_color/')),
                ('price', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'core_kitchen_color',
                'verbose_name': 'Kitchen Color',
                'verbose_name_plural': 'Kitchen Colors',
            },
        ),
        migrations.CreateModel(
            name='KFinishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'core_kitchen_finishing',
                'verbose_name': 'Kitchen Finishing',
                'verbose_name_plural': 'Kitchen Finishings',
            },
        ),
        migrations.CreateModel(
            name='KImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='kitchen/images/kitchen_images/')),
                ('k_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kithen_image', to='core.KColor')),
            ],
            options={
                'ordering': ['kitchen', 'k_color'],
                'db_table': 'core_kitchen_image',
                'verbose_name': 'Kitchen Image',
                'verbose_name_plural': 'Kitchen Images',
            },
        ),
        migrations.CreateModel(
            name='KIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('items', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='kitchen/images/kitchen_appliances/')),
            ],
            options={
                'ordering': ['kitchen', 'name', 'brand'],
                'db_table': 'core_kitchen_include',
                'verbose_name': 'Kitchen Include',
                'verbose_name_plural': 'Kitchen Includes',
            },
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('desc', models.CharField(max_length=100, verbose_name='Description')),
                ('l', models.IntegerField(verbose_name='length')),
                ('b', models.IntegerField(verbose_name='breadth')),
                ('h', models.IntegerField(verbose_name='height')),
                ('slug', models.SlugField(editable=False, max_length=200, null=True)),
            ],
            options={
                'ordering': ['name', 'theme'],
                'db_table': 'core_kitchen',
                'verbose_name': 'Kitchen',
                'verbose_name_plural': 'Kitchens',
            },
        ),
        migrations.CreateModel(
            name='KMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('price', models.IntegerField()),
            ],
            options={
                'ordering': ('name', 'price'),
                'db_table': 'core_kitchen_material',
                'verbose_name': 'Kitchen material',
                'verbose_name_plural': 'Kitchen Materials',
            },
        ),
        migrations.CreateModel(
            name='KTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Theme Name')),
                ('desc', models.CharField(max_length=100, verbose_name='Description')),
                ('image', models.ImageField(upload_to='kitchen/images/kitchen_themes/')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'core_kitchen_theme',
                'verbose_name': 'Kitchen Theme',
                'verbose_name_plural': 'Kitchen Themes',
            },
        ),
        migrations.CreateModel(
            name='KType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Type Name')),
                ('image', models.ImageField(upload_to='kitchen/images/kitchen_types/')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'core_kitchen_type',
                'verbose_name': 'Kitchen Type',
                'verbose_name_plural': 'Kitchen Types',
            },
        ),
        migrations.AddField(
            model_name='ktheme',
            name='k_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='k_type', to='core.KType'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theme', to='core.KTheme'),
        ),
        migrations.AddField(
            model_name='kincludes',
            name='kitchen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Kitchen'),
        ),
        migrations.AddField(
            model_name='kimage',
            name='kitchen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kitchen', to='core.Kitchen'),
        ),
        migrations.AddField(
            model_name='kappliance',
            name='kitchen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Kitchen'),
        ),
        migrations.AlterUniqueTogether(
            name='ktheme',
            unique_together=set([('k_type', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='kitchen',
            unique_together=set([('theme', 'slug', 'l', 'b', 'h')]),
        ),
        migrations.AlterUniqueTogether(
            name='kappliance',
            unique_together=set([('kitchen', 'name')]),
        ),
    ]
