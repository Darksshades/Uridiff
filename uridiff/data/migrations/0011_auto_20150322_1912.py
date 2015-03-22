# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_auto_20150322_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionusers',
            name='submission_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
