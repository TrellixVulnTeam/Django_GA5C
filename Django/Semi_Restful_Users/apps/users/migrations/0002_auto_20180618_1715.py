# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-18 22:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='emails',
            new_name='email',
        ),
    ]