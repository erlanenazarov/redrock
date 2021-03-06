# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-07 17:06
from __future__ import unicode_literals

import base.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=base.models.image_upload_to)),
                ('link', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=base.models.image_upload_to)),
                ('description', models.TextField()),
                ('url', models.URLField(max_length=10000)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Information',
                'verbose_name_plural': 'Main information',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=base.models.image_upload_to)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Image',
                'verbose_name_plural': 'Slider Images',
            },
        ),
        migrations.CreateModel(
            name='ThingsToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=base.models.image_upload_to)),
                ('tours', models.ManyToManyField(to='base.Tour')),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'THINGS TO DO',
            },
        ),
        migrations.CreateModel(
            name='TripPlanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True, null=True)),
                ('initial', models.DateField()),
                ('final', models.DateField()),
                ('people', models.IntegerField(default=1)),
                ('children', models.IntegerField(default=0)),
                ('category_of_tour', models.CharField(blank=True, choices=[('Luxe', 'Luxe'), ('Standart', 'Standart'), ('Budget', 'Budget')], max_length=100, null=True)),
                ('transport', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100, null=True)),
                ('food', models.CharField(blank=True, choices=[('Full board', 'Full board'), ('Half board', 'Half board'), ('Bed breakfast', 'Bed breakfast'), ('Room only', 'Room only')], max_length=100, null=True)),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Hotel')),
                ('tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Tour')),
            ],
            options={
                'verbose_name': 'TRIP PLANNER',
                'verbose_name_plural': 'Trip Planner',
            },
        ),
    ]
