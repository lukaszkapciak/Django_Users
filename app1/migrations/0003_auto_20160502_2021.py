# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='NA', upload_to='app1/templates'),
        ),
    ]