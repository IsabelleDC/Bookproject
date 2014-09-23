# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20140922_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='image',
            field=models.ImageField(null=True, upload_to=b'livre_ image', blank=True),
        ),
    ]
