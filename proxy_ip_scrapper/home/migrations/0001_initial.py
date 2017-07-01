# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IPdata',
            fields=[
                ('ip_address', models.GenericIPAddressField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100)),
                ('port_no', models.PositiveIntegerField()),
                ('anonymity', models.CharField(default='Low', max_length=50)),
                ('HTTPS', models.CharField(default='Not Specified', max_length=50)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]