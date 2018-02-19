# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infila', '0003_auto_20141201_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='delay',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
