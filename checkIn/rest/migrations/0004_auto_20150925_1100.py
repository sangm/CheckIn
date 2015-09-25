# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_auto_20150925_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rawstudentdata',
            name='id',
        ),
        migrations.AlterField(
            model_name='rawstudentdata',
            name='username',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
    ]
