# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20150322_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionusers',
            name='submission_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
