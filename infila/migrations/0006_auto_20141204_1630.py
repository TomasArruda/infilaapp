# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infila', '0005_auto_20141201_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='PToken',
            fields=[
                ('token', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to='infila.Admin')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='token',
            name='user',
            field=models.ForeignKey(to='infila.Patient'),
            preserve_default=True,
        ),
    ]
