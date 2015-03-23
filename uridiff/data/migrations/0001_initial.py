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
                ('solved', models.CharField(max_length=10, blank=True)),
                ('level', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionUsers',
            fields=[
                ('submission_date', models.CharField(max_length=32, blank=True)),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('question', models.ForeignKey(related_name='users', to='data.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UriUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('avatar_url', models.CharField(max_length=128, blank=True)),
                ('position', models.IntegerField(default=0)),
                ('last_page', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='questionusers',
            name='user',
            field=models.ForeignKey(related_name='questions', to='data.UriUser'),
            preserve_default=True,
        ),
    ]
