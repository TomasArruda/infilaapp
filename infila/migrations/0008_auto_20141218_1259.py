# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infila', '0007_appointment_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ptoken',
            name='user',
            field=models.ForeignKey(to='infila.Patient'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='token',
            name='user',
            field=models.ForeignKey(to='infila.Admin'),
            preserve_default=True,
        ),
    ]
