# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-23 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0014_auto_20160922_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subgenreclassalbumrelationship',
            name='page',
        ),
        migrations.RemoveField(
            model_name='subgenreclassalbumrelationship',
            name='subgenre',
        ),
        migrations.DeleteModel(
            name='SubGenreClassAlbumRelationship',
        ),
    ]
