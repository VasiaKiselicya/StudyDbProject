# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-03 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsiblepersons',
            name='phone_number',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='responsiblepersons',
            name='premium',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='responsiblepersons',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
