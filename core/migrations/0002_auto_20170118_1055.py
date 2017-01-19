# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 10:55
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
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
                'verbose_name': 'Kitchen Appliance',
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
                ('category', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='kitchen/images/kitchen_appliances/')),
            ],
            options={
                'ordering': ['kitchen', 'category', 'brand'],
                'db_table': 'core_kitchen_include',
                'verbose_name': 'Kitchen Include',
                'verbose_name_plural': 'Kitchen Includes',
            },
        ),
        migrations.CreateModel(
            name='KISub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=30)),
                ('is_inculded', models.BooleanField(default=True)),
                ('k_includes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.KIncludes')),
            ],
            options={
                'abstract': False,
            },
        ),
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
                ('k_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='k_type', to='core.KType')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'core_kitchen_theme',
                'verbose_name': 'Kitchen Theme',
                'verbose_name_plural': 'Kitchen Themes',
            },
        ),
        migrations.CreateModel(
            name='WAppliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='wardrobe/images/wardrobe_appliances/')),
            ],
            options={
                'ordering': ('name', 'wardrobe'),
                'db_table': 'core_wardrobe_appliance',
                'verbose_name': 'Wardrobe Apliance',
                'verbose_name_plural': 'Wardrobe Appliances',
            },
        ),
        migrations.CreateModel(
            name='Wardrobe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('desc', models.CharField(max_length=100, verbose_name='Description')),
                ('l', models.IntegerField(verbose_name='length')),
                ('b', models.IntegerField(verbose_name='breadth')),
                ('h', models.IntegerField(verbose_name='height')),
                ('base_price', models.IntegerField(verbose_name='Base Price')),
                ('min_change', models.IntegerField(default=20, verbose_name='Miniumum Change')),
                ('max_change', models.IntegerField(default=40, verbose_name='Maximum Change')),
                ('slug', models.SlugField(editable=False, max_length=200, null=True)),
            ],
            options={
                'ordering': ['name', 'theme'],
                'db_table': 'core_wardrobe',
                'verbose_name': 'Wardrobe',
                'verbose_name_plural': 'Wardrobes',
            },
        ),
        migrations.CreateModel(
            name='WColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('image', models.ImageField(upload_to='wardrobe/images/wardrobe_color/')),
                ('price', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'core_wardrobe_color',
                'verbose_name': 'Wardrobe Color',
                'verbose_name_plural': 'Wardrobe Colors',
            },
        ),
        migrations.CreateModel(
            name='WFinishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'core_wardrobe_finishing',
                'verbose_name': 'Wardrobe Finishing',
                'verbose_name_plural': 'Wardrobe Finishings',
            },
        ),
        migrations.CreateModel(
            name='WImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='wardrobe/images/wardrobe_images/')),
                ('w_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wardrobe_image', to='core.WColor')),
                ('wardrobe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wardrobe', to='core.Wardrobe')),
            ],
            options={
                'ordering': ['wardrobe', 'w_color'],
                'db_table': 'core_wardrobe_image',
                'verbose_name': 'Kitchen Image',
                'verbose_name_plural': 'Wardrobe Images',
            },
        ),
        migrations.CreateModel(
            name='WIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='wardrobe/images/wardrobe_appliances/')),
                ('wardrobe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Wardrobe')),
            ],
            options={
                'ordering': ['wardrobe', 'category', 'brand'],
                'db_table': 'core_wardrobe_include',
                'verbose_name': 'Wardrobe Include',
                'verbose_name_plural': 'Wardrobe Includes',
            },
        ),
        migrations.CreateModel(
            name='WISub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=30)),
                ('is_inculded', models.BooleanField(default=True)),
                ('w_includes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.WIncludes')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('price', models.IntegerField()),
            ],
            options={
                'ordering': ('name', 'price'),
                'db_table': 'core_wardrobe_material',
                'verbose_name': 'Wardrobe material',
                'verbose_name_plural': 'Wardrobe Materials',
            },
        ),
        migrations.CreateModel(
            name='WTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Theme Name')),
                ('desc', models.CharField(max_length=100, verbose_name='Description')),
                ('image', models.ImageField(upload_to='wardrobe/images/wardrobe_themes/')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'core_wardrobe_theme',
                'verbose_name': 'Wardrobe Theme',
                'verbose_name_plural': 'Wardrobe Themes',
            },
        ),
        migrations.CreateModel(
            name='WType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Type Name')),
                ('image', models.ImageField(upload_to='wardrobe/images/wardrobe_types/')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'core_wardrobe_type',
                'verbose_name': 'Wardrobe Type',
                'verbose_name_plural': 'Wardrobe Types',
            },
        ),
        migrations.AddField(
            model_name='wtheme',
            name='w_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='w_type', to='core.WType'),
        ),
        migrations.AddField(
            model_name='wardrobe',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theme', to='core.WTheme'),
        ),
        migrations.AddField(
            model_name='wappliance',
            name='wardrobe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Wardrobe'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Theme', to='core.KTheme'),
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
            name='wtheme',
            unique_together=set([('w_type', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='wardrobe',
            unique_together=set([('theme', 'slug', 'l', 'b', 'h')]),
        ),
        migrations.AlterUniqueTogether(
            name='wappliance',
            unique_together=set([('wardrobe', 'name')]),
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
