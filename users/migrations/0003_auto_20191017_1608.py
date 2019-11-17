# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-17 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191017_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='firstName',
            field=models.CharField(default='First Name', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='homeAddress',
            field=models.CharField(default='Your home address', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastName',
            field=models.CharField(default='Last Name', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='phoneNumber',
            field=models.CharField(default='0766 xxx xxx', max_length=20),
        ),
    ]