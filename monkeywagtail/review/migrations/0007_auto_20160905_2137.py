# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-05 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_auto_20160628_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewpage',
            name='date',
        ),
        migrations.AddField(
            model_name='reviewpage',
            name='date_release',
            field=models.DateField(blank=True, null=True, verbose_name='Release date of album'),
        ),
        migrations.AddField(
            model_name='reviewpage',
            name='song_details',
            field=wagtail.wagtailcore.fields.StreamField((('SongBlock', wagtail.wagtailcore.blocks.StructBlock((('album_song', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='e.g. Waiting Room', required=False)), ('album_song_length', wagtail.wagtailcore.blocks.TimeBlock(blank=True, required=False))), icon='openquote', template='blocks/songstreamblock.html')),), blank=True),
        ),
    ]
