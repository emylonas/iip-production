# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iip_smr_web_app', '0003_auto_20171010_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPage2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100)),
                ('title_header', models.CharField(blank=True, max_length=100)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('content', models.TextField(blank=True, help_text='Markdown allowed.')),
            ],
            options={
                'verbose_name_plural': 'Static Pages',
            },
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]