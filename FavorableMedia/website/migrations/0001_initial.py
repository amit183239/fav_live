# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-09 12:14
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(default=datetime.datetime(2016, 11, 9, 12, 14, 23, 529192), editable=False)),
                ('updated_on', models.DateTimeField(default=datetime.datetime(2016, 11, 9, 12, 14, 23, 529232), editable=False)),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('url', models.CharField(blank=True, max_length=300, null=True)),
                ('image_link', models.CharField(blank=True, max_length=300, null=True)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
