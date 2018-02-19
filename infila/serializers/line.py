from django.contrib.auth.models import User, Group
from rest_framework import serializers
from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token

class LineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Line
        fields = ('id', 'date', 'active', 'medic', 'clinic', 'avarageTime')