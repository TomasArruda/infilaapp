from django.contrib.auth.models import User, Group
from rest_framework import serializers
from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token

class MedicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medic
        fields = ('id', 'name', 'crm', 'speciality', 'email')