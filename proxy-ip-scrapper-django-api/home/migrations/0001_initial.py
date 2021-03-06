# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 06:10
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('country', models.CharField(max_length=100)),
                ('port_no', models.PositiveIntegerField()),
                ('anonimity', models.CharField(default='Low', max_length=50)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('HTTPS', models.CharField(default='No', max_length=3)),
            ],
        ),
    ]
