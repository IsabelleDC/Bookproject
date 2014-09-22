# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20140922_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('streetnum', models.IntegerField(null=True, blank=True)),
                ('street', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('country', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField(max_length=10, null=True, blank=True)),
                ('categories', models.ManyToManyField(related_name=b'livres', to='book.Genre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='genre',
            name='user',
            field=models.ForeignKey(related_name=b'genres', default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitor',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=b'profile_picture', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
