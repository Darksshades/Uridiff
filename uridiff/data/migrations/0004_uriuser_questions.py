# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_uriuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='uriuser',
            name='questions',
            field=models.ManyToManyField(to='data.Question'),
            preserve_default=True,
        ),
    ]
