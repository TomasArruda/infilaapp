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

class Clinic(models.Model):
	name = models.CharField(max_length=100, blank=False, default='', null=False)
	cnpj = models.CharField(max_length=100, blank=False, default='', null=False)
	speciality = models.CharField(max_length=100, blank=False, default='', null=False)
	socialReason = models.CharField(max_length=100, blank=False, default='', null=False)
	
	address = models.CharField(max_length=100, blank=False, default='', null=False)
	number = models.CharField(max_length=100, blank=False, default='', null=False)
	complement = models.CharField(max_length=100, blank=False, default='', null=False)
	neighbourhood = models.CharField(max_length=100, blank=False, default='', null=False)
	city = models.CharField(max_length=100, blank=False, default='', null=False)
	state = models.CharField(max_length=100, blank=False, default='', null=False)
	zipcode = models.CharField(max_length=100, blank=False, default='', null=False)
	site = models.CharField(max_length=100, blank=True, null=True)
	
	phoneNumber = PhoneNumberField()
	medics = models.ManyToManyField('Medic')
	class  Meta:
		ordering = ('name',)