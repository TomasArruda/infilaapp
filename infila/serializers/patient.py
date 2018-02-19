from django.contrib.auth.models import User, Group
from rest_framework import serializers
from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'name', 'email', 'phoneNumber', 'password', 'gcm_id')
