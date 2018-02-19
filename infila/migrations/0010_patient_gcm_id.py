# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infila', '0009_pnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gcm_id',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
