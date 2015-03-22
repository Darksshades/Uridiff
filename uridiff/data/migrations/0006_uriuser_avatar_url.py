# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20150322_0553'),
    ]

    operations = [
        migrations.AddField(
            model_name='uriuser',
            name='avatar_url',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
