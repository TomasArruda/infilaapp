from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from datetime import date
from django.core.mail import send_mail
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
import binascii
import os

class Appointment(models.Model):
	time = models.TimeField(auto_now=False, null=False, blank=False, default='00:00')  #pattern hh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]
	name = models.CharField(max_length=100, blank=False, default='', null=False)
	patient = models.ForeignKey('Patient', blank = True, null = True)
	line = models.ForeignKey('Line', default='')
	delay = models.IntegerField(default = 0)
	check = models.BooleanField(default=False)

	appointment_type = models.CharField(max_length=100, blank=True, null=True)
	phoneNumber = PhoneNumberField(null=True, blank = True, unique = False)

	def __unicode__(self):
		return unicode(self.patient.PhoneNumber)

	class  Meta:
		ordering = ('line','time')
		unique_together = ("time", "line")