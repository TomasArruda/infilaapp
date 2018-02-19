# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infila', '0014_auto_20150204_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotification',
            name='admin',
            field=models.ForeignKey(default=b'', blank=True, to='infila.Admin'),
            preserve_default=True,
        ),
    ]
