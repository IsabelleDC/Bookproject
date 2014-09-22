# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20140922_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='position',
            field=geoposition.fields.GeopositionField(default='', max_length=42),
            preserve_default=False,
        ),
    ]
