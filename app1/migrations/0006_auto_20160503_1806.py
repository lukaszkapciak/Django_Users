# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20160503_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]