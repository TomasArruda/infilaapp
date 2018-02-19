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

class Line(models.Model):
	date = models.DateField(auto_now=False, null=False, blank=False)
	active = models.BooleanField(default=True)
	medic = models.ForeignKey('Medic',default='')
	clinic = models.ForeignKey('Clinic',default='')
	avarageTime = models.IntegerField(default=30)
	class  Meta:
		ordering = ('date',)
		unique_together = ("date", "medic", "clinic")