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

class ANotification(models.Model):
	flag = models.CharField(max_length=200, blank=False, default='', null=False)
	text = models.CharField(max_length=200, blank=False, default='', null=False)
	admin = models.ForeignKey('Admin', blank=True, null=True)
	class  Meta:
		ordering = ('id',)