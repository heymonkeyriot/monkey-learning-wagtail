# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-02 21:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourpage',
            old_name='image',
            new_name='tour_image',
        ),
        migrations.AddField(
            model_name='tourdates',
            name='city',
            field=models.CharField(blank=True, help_text='City of the venue', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tourdates',
            name='country',
            field=models.CharField(choices=[('austria', 'Austria'), ('belgium', 'Belgium'), ('denmark', 'Denmark'), ('finland', 'Finland'), ('france', 'France'), ('germany', 'Germany'), ('greece', 'Greece'), ('iceland', 'Iceland'), ('ireland', 'Ireland'), ('italy', 'Italy'), ('netherlands', 'Netherlands'), ('norway', 'Norway'), ('poland', 'Poland'), ('portugal', 'Portugal'), ('serbia', 'Serbia'), ('slovakia', 'Slovakia'), ('slovenia', 'Slovenia'), ('spain', 'Spain'), ('sweden', 'Sweden'), ('switzerland', 'Switzerland'), ('uk', 'United Kingdom (UK)')], default=datetime.datetime(2017, 2, 2, 21, 42, 40, 8365, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tourdates',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tourdates',
            name='door_open',
            field=models.TimeField(blank=True, help_text='Time show starts', null=True),
        ),
        migrations.AddField(
            model_name='tourdates',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tourdates',
            name='venue',
            field=models.CharField(help_text='Name of the venue', max_length=255),
        ),
    ]
