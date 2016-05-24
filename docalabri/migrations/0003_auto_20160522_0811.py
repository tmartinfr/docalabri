# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-22 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docalabri', '0002_contact_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(error_messages={b'unique': b'Cette adresse e-mail est d\xc3\xa9j\xc3\xa0 enregistr\xc3\xa9e'}, max_length=254, unique=True),
        ),
    ]