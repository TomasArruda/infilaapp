# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infila', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinic',
            old_name='street',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='country',
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='details',
        ),
        migrations.RemoveField(
            model_name='line',
            name='details',
        ),
        migrations.AddField(
            model_name='clinic',
            name='complement',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clinic',
            name='neighbourhood',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clinic',
            name='site',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clinic',
            name='socialReason',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clinic',
            name='specility',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='medic',
            name='email',
            field=models.EmailField(default=b'', max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
