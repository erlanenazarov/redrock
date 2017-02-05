# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-21 21:02
from __future__ import unicode_literals

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=base.models.image_upload_to)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
    ]