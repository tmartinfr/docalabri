# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0010_auto_20160524_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
