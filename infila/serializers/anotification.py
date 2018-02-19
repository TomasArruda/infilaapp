from django.contrib.auth.models import User, Group
from rest_framework import serializers
from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token, PNotification, ANotification

class ANotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ANotification
        fields = ('id','flag' , 'text', 'admin')