from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from datetime import date
from django.core.mail import send_mail
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, User)
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
import binascii
import os
from django.contrib.auth.hashers import *

class Admin(AbstractBaseUser):
	login = models.CharField(max_length=100, blank=False, default='', null=False, unique=True)
	email = models.EmailField(blank=True, default='')
	clinic = models.ForeignKey('Clinic', default='')
	USERNAME_FIELD = 'login'
	REQUIRED_FIELDS = ['email', 'password']

	def save(self, *args, **kwargs):
		self.password = make_password(self.password)
		super(Admin, self).save(*args, **kwargs)

	def email_user(self, subject, message, from_email=None):
		"""
		Sends an email to this User.
		"""
		send_mail(subject, message, from_email, [self.email])

	class  Meta:
		ordering = ('id',)