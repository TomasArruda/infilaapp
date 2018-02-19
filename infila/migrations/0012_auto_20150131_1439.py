# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infila', '0011_auto_20150131_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='appountment_type',
            new_name='appointment_type',
        ),
    ]
