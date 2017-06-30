# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170614_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipdata',
            name='id',
        ),
        migrations.AlterField(
            model_name='ipdata',
            name='ip_address',
            field=models.GenericIPAddressField(primary_key=True, serialize=False),
        ),
    ]
