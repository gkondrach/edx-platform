# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 12:10
from __future__ import absolute_import, unicode_literals

from django.db import migrations
import jsonfield.fields
import opaque_keys.edx.django.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_comment_common', '0006_coursediscussionsettings_discussions_id_map'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscussionsIdMapping',
            fields=[
                ('course_id', opaque_keys.edx.django.models.CourseKeyField(db_index=True, max_length=255, primary_key=True, serialize=False)),
                ('mapping', jsonfield.fields.JSONField(help_text=b'Key/value store mapping discussion IDs to discussion XBlock usage keys.')),
            ],
            options={
                'db_table': 'django_comment_common_discussionsidmapping',
            },
        ),
    ]