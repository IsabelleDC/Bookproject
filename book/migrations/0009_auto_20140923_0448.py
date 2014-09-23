# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20140923_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livre',
            name='street',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='streetnum',
        ),
    ]
