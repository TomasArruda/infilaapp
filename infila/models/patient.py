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
from django.contrib.auth.hashers import *

class Patient(AbstractBaseUser):
    name = models.CharField(max_length=100, blank=False, default='', null=False)
    phoneNumber = PhoneNumberField(null=False, unique = True)
    email = models.EmailField(blank=True, default='')
    USERNAME_FIELD = 'phoneNumber'
    REQUIRED_FIELDS = ['email', 'password']
    gcm_id = models.TextField(max_length=None,default='')

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Patient, self).save(*args, **kwargs)
    
    def email_user(self, subject, message, from_email=None):
		"""
		Sends an email to this User.
		"""
		send_mail(subject, message, from_email, [self.email])

    def __unicode__(self):
        return unicode(self.phoneNumber)

    class Meta:
        ordering = ('id',)