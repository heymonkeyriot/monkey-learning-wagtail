# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-05 21:01
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_auto_20160905_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewpage',
            name='song_details',
            field=wagtail.wagtailcore.fields.StreamField((('SongBlock', wagtail.wagtailcore.blocks.StructBlock((('album_song', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='e.g. Waiting Room', required=False)), ('album_song_length', wagtail.wagtailcore.blocks.TimeBlock(blank=True, required=False))), icon='openquote', template='blocks/songstreamblock.html', title='Song')),), blank=True, verbose_name='Songs'),
        ),
    ]
