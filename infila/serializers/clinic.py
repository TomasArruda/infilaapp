from django.contrib.auth.models import User, Group
from rest_framework import serializers
from infila.models import Patient, Appointment, Clinic, Medic, Line, Admin, Token
#from medic import MedicSerializer

class ClinicSerializer(serializers.HyperlinkedModelSerializer):
    #medics = MedicSerializer(many=True, allow_add_remove=True, read_only=False)
    class Meta:
        model = Clinic
        fields = ('id', 'name', 'cnpj', 'speciality', 'socialReason','address', 'number', 'complement', 'city', 'neighbourhood', 'state', 'zipcode', 'phoneNumber', 'medics')
