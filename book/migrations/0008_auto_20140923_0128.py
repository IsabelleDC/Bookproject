# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20140923_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='author',
            field=models.TextField(max_length=30, null=True, blank=True),
        ),
    ]
