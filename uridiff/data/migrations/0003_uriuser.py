# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20150322_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='UriUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
