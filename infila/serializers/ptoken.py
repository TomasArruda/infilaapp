from django.contrib.auth.models import User, Group
from rest_framework import serializers
from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token, PToken

class PTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PToken
        fields = ('user', 'token', 'created')