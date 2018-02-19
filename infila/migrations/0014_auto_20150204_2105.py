# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infila', '0013_anotification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anotification',
            old_name='admins',
            new_name='admin',
        ),
    ]
