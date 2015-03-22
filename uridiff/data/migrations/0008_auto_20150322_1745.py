# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_uriuser_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionUsers',
            fields=[
                ('submission_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('question', models.ForeignKey(to='data.Question')),
                ('user', models.ForeignKey(to='data.UriUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='uriuser',
            name='questions',
        ),
    ]
