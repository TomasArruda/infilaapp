# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('infila', '0010_patient_gcm_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appountment_type',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
    ]
