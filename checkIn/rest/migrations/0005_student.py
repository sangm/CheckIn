# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_auto_20150925_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('username', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('givenname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
