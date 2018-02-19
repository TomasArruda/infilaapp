from django.contrib.auth.models import User, Group
from rest_framework import serializers
from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token, PNotification

class PNotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PNotification
        fields = ('id', 'text', 'patients')