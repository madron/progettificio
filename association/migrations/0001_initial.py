# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=200, verbose_name='cognome')),
                ('name', models.CharField(max_length=200, verbose_name='nome')),
            ],
            options={
                'ordering': ('surname', 'name'),
                'verbose_name': 'socio',
                'verbose_name_plural': 'soci',
            },
        ),
    ]
