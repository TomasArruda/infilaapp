# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infila', '0015_auto_20150204_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotification',
            name='admin',
            field=models.ForeignKey(blank=True, to='infila.Admin', null=True),
            preserve_default=True,
        ),
    ]
