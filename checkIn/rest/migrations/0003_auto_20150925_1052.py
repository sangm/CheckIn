# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20150925_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawstudentdata',
            name='course1',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='rawstudentdata',
            name='course2',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='rawstudentdata',
            name='course3',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
