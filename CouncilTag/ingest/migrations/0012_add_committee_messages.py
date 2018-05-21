# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-08 00:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0011_add_eth_to_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='email',
            field=models.CharField(default='counciltag@gmail.com', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='committee',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='ingest.Committee'),
        ),
    ]