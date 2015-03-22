# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='resolved',
        ),
        migrations.AddField(
            model_name='question',
            name='solved',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
