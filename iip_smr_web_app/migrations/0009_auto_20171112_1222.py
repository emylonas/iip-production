# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-12 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iip_smr_web_app', '0008_auto_20171025_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storypage',
            name='image',
        ),
        migrations.AddField(
            model_name='storypage',
            name='thumbnail_url',
            field=models.TextField(blank=True),
        ),
    ]
