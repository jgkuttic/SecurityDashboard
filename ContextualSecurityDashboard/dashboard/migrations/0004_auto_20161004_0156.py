# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-04 01:56
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20161004_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportitem',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reportitem',
            name='categories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None),
        ),
        migrations.AlterField(
            model_name='reportitem',
            name='content',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reportitem',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reportitem',
            name='guid',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reportitem',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reportitem',
            name='pubDate',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reportitem',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reportitem',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
