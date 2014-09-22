# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_visitor_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livre',
            old_name='categories',
            new_name='genres',
        ),
        migrations.AddField(
            model_name='livre',
            name='author',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='livre',
            name='image',
            field=models.ImageField(null=True, upload_to=b'livre image', blank=True),
            preserve_default=True,
        ),
    ]
