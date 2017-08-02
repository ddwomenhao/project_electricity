# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(help_text=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True)),
                ('update_time', models.DateTimeField(help_text=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', auto_now=True)),
                ('is_delete', models.BooleanField(default=False, help_text=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('username', models.CharField(help_text=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d', max_length=20)),
                ('password', models.CharField(help_text=b'\xe5\xaf\x86\xe7\xa0\x81', max_length=40)),
                ('email', models.EmailField(help_text=b'\xe9\x82\xae\xe7\xae\xb1', max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
