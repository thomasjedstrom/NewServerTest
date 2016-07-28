# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 16:49
from __future__ import unicode_literals

import apps.accounts.mixins
import apps.accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True, validators=[apps.accounts.models.validateLengthGreaterThanTwo])),
                ('first_name', models.CharField(max_length=100, validators=[apps.accounts.models.validateLengthGreaterThanTwo])),
                ('last_name', models.CharField(max_length=100, validators=[apps.accounts.models.validateLengthGreaterThanTwo])),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=255, validators=[apps.accounts.models.validateLengthGreaterThanTwo])),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'users',
            },
            bases=(apps.accounts.mixins.CustomMixin, models.Model),
        ),
    ]