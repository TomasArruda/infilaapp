# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infila', '0004_appointment_delay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='delay',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
