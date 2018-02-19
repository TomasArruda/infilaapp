# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infila', '0006_auto_20141204_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='check',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
