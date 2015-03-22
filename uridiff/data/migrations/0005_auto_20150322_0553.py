# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_uriuser_questions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uriuser',
            old_name='username',
            new_name='name',
        ),
    ]
