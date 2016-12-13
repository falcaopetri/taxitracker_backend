# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-13 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=10)),
                ('login', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=30)),
            ],
        ),
    ]
