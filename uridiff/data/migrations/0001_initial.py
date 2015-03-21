# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('category', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('resolved', models.FloatField()),
                ('level', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
