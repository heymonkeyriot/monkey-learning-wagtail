# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-11 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feature_content_page', '0002_auto_20160708_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistfeaturepagerelationship',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.Artist'),
        ),
    ]
