# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-05 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170202_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='description',
            field=models.TextField(),
        ),
    ]
