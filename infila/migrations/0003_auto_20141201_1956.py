# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infila', '0002_auto_20141201_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinic',
            old_name='specility',
            new_name='speciality',
        ),
    ]
