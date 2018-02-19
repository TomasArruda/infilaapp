from django.contrib.auth.models import User, Group
from rest_framework import serializers
from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token

class AppointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'time', 'name', 'patient', 'line', 'delay', 'check', 'appointment_type', 'phoneNumber')