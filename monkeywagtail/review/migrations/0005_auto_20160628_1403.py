# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-28 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_reviewauthorrelationship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewauthorrelationship',
            old_name='author_name',
            new_name='author',
        ),
    ]
