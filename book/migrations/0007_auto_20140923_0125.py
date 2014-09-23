# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20140922_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='author',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='livre',
            name='image',
            field=models.ImageField(null=True, upload_to=b'livre_image', blank=True),
        ),
    ]
