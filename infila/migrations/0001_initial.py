# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('login', models.CharField(default=b'', unique=True, max_length=100)),
                ('email', models.EmailField(default=b'', max_length=75, blank=True)),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField(default=b'00:00')),
                ('name', models.CharField(default=b'', max_length=100)),
            ],
            options={
                'ordering': ('line', 'time'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('cnpj', models.CharField(default=b'', max_length=100)),
                ('details', models.TextField()),
                ('street', models.CharField(default=b'', max_length=100)),
                ('number', models.CharField(default=b'', max_length=100)),
                ('city', models.CharField(default=b'', max_length=100)),
                ('state', models.CharField(default=b'', max_length=100)),
                ('country', models.CharField(default=b'', max_length=100)),
                ('zipcode', models.CharField(default=b'', max_length=100)),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('details', models.TextField()),
                ('date', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('avarageTime', models.IntegerField(default=30)),
                ('clinic', models.ForeignKey(default=b'', to='infila.Clinic')),
            ],
            options={
                'ordering': ('date',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('crm', models.CharField(default=b'', max_length=100)),
                ('speciality', models.CharField(default=b'', max_length=100)),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(unique=True, max_length=128)),
                ('email', models.EmailField(default=b'', max_length=75, blank=True)),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to='infila.Admin')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='line',
            name='medic',
            field=models.ForeignKey(default=b'', to='infila.Medic'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='line',
            unique_together=set([('date', 'medic', 'clinic')]),
        ),
        migrations.AddField(
            model_name='clinic',
            name='medics',
            field=models.ManyToManyField(to='infila.Medic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='line',
            field=models.ForeignKey(default=b'', to='infila.Line'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(blank=True, to='infila.Patient', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together=set([('time', 'line')]),
        ),
        migrations.AddField(
            model_name='admin',
            name='clinic',
            field=models.ForeignKey(default=b'', to='infila.Clinic'),
            preserve_default=True,
        ),
    ]
