# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20150322_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionusers',
            name='question',
            field=models.ForeignKey(related_name='users', to='data.Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questionusers',
            name='user',
            field=models.ForeignKey(related_name='questions', to='data.UriUser'),
            preserve_default=True,
        ),
    ]
