# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forman', '0002_auto_20170502_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='display_type',
            field=models.CharField(choices=[('text', 'text'), ('image', 'image'), ('password', 'password'), ('radio', 'radio'), ('submit', 'submit'), ('reset', 'reset'), ('textarea', 'textarea'), ('file', 'file'), ('select', 'select'), ('multi-select', 'multi-select'), ('checkbox', 'checkbox')], max_length=100),
        ),
    ]