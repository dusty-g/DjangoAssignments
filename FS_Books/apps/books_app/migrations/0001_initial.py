# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-19 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=220)),
                ('author', models.TextField(max_length=220)),
                ('category', models.TextField(max_length=220)),
            ],
        ),
    ]
