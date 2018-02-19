# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infila', '0012_auto_20150131_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='ANotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flag', models.CharField(default=b'', max_length=200)),
                ('text', models.CharField(default=b'', max_length=200)),
                ('admins', models.ForeignKey(default=b'', to='infila.Admin')),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
    ]
